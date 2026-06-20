from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
# Recommended:
# set GROQ_API_KEY in environment variables
# Windows:
# set GROQ_API_KEY=your_key
#
# Linux/Mac:
# export GROQ_API_KEY=your_key

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_response(
    prompt: str,
    model: str = "llama-3.3-70b-versatile",
    temperature: float = 0.7,
):
    """
    Generate response from Groq LLM
    """

    try:
        response = client.chat.completions.create(
            model=model,
            temperature=temperature,
            messages=[
                {
                    "role": "system",
                    "content": """
You are an AI workflow assistant.
Provide clear, concise, and accurate responses.
""",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        return {
            "success": True,
            "response": response.choices[0].message.content,
        }

    except Exception as e:
        print("Groq Error:", str(e))

        return {
            "success": False,
            "response": f"Error: {str(e)}",
        }