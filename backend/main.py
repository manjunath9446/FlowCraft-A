from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from collections import defaultdict, deque
from groq import Groq
from dotenv import load_dotenv
import os

# =====================================
# Load Environment Variables
# =====================================

load_dotenv()

# =====================================
# FastAPI App
# =====================================

app = FastAPI()

# =====================================
# CORS
# =====================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================
# Groq Client
# =====================================

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# =====================================
# Models
# =====================================

class PipelineRequest(BaseModel):
    nodes: List[dict]
    edges: List[dict]


class LLMRequest(BaseModel):
    prompt: str
    model: str = "llama-3.3-70b-versatile"


# =====================================
# Root
# =====================================

@app.get("/")
def root():
    return {
        "message": "FlowCraft Backend Running"
    }


# =====================================
# DAG Validation
# =====================================

def is_dag(nodes, edges):
    graph = defaultdict(list)
    indegree = defaultdict(int)

    for node in nodes:
        indegree[node["id"]] = 0

    for edge in edges:
        graph[edge["source"]].append(
            edge["target"]
        )
        indegree[
            edge["target"]
        ] += 1

    queue = deque(
        [
            node_id
            for node_id in indegree
            if indegree[node_id] == 0
        ]
    )

    visited = 0

    while queue:
        current = queue.popleft()
        visited += 1

        for neighbor in graph[current]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return visited == len(nodes)


# =====================================
# Parse Pipeline
# =====================================

@app.post("/pipelines/parse")
def parse_pipeline(
    data: PipelineRequest
):
    return {
        "num_nodes": len(data.nodes),
        "num_edges": len(data.edges),
        "is_dag": is_dag(
            data.nodes,
            data.edges
        ),
    }


# =====================================
# LLM Endpoint
# =====================================

@app.post("/llm")
def run_llm(data: LLMRequest):
    try:

        print("\n========== PROMPT ==========")
        print(data.prompt)
        print("============================\n")

        completion = (
            client.chat.completions.create(
                model=data.model,
                temperature=0.7,
                messages=[
                    {
                        "role": "system",
                        "content": """
You are a helpful AI assistant.

Return plain text only.
Do not use markdown.
Do not use **bold** text.
Do not use headings.
Keep responses concise and readable.
"""
                    },
                    {
                        "role": "user",
                        "content": data.prompt
                    }
                ]
            )
        )

        response = (
            completion
            .choices[0]
            .message
            .content
        )

        return {
            "success": True,
            "response": response
        }

    except Exception as e:
        print(e)

        return {
            "success": False,
            "response": str(e)
        }