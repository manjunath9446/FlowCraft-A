# 🚀 FlowCraft AI

A visual AI workflow orchestration platform that enables users to design, connect, and execute AI pipelines using a drag-and-drop interface.

FlowCraft AI simplifies prompt engineering and workflow automation by allowing users to visually connect Input, Prompt, LLM, and Output nodes on an interactive canvas.

---

## ✨ Features

### 🎨 Visual Workflow Builder

* Drag-and-drop node creation
* Interactive React Flow canvas
* Dynamic node connections
* Infinite workflow design space

### 🧠 AI Workflow Execution

* Input Node
* Prompt Node
* LLM Node
* Output Node
* Sequential workflow execution

### ⚡ Prompt Engineering

Supports dynamic variable injection using placeholders.

Example:

```text
Write a professional blog about {{input}}
```

Variables are automatically replaced during workflow execution.

### 🔍 Workflow Validation

* DAG validation
* Invalid connection detection
* Execution path verification
* Workflow integrity checks

### 📊 Node Inspector

* Edit node properties
* Configure prompt templates
* Select model providers
* Modify workflow settings

### 📜 Execution Console

* Real-time workflow logs
* Execution tracking
* Status updates
* Debug information

### 🌐 Modern Landing Page

* SaaS-inspired UI
* Animated workflow demonstrations
* Product overview sections
* Builder integration

---

## 🏗️ Architecture

### Workflow Architecture

```text
User Input
    │
    ▼
Input Node
    │
    ▼
Prompt Node
    │
    ▼
LLM Node
    │
    ▼
Output Node
```

### System Architecture

```text
Frontend (React + React Flow)
            │
            ▼
     FastAPI Backend
            │
            ▼
      Groq / OpenAI
```

---

## 🛠️ Tech Stack

### Frontend

* React.js
* React Flow
* Zustand
* React Router
* Framer Motion
* CSS3

### Backend

* FastAPI
* Python
* NetworkX
* Pydantic
* Groq API
* OpenAI API

### Deployment

* Vercel (Frontend)
* Render (Backend)

---

## 📂 Project Structure

```text
flowcraft-ai/
│
├── frontend/
│   ├── src/
│   │   ├── nodes/
│   │   ├── layout/
│   │   ├── pages/
│   │   ├── styles/
│   │   ├── ui.js
│   │   ├── store.js
│   │   └── App.js
│   │
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── main.py
│   ├── workflow_executor.py
│   ├── requirements.txt
│   └── .env
│
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/flowcraft-ai.git
cd flowcraft-ai
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm start
```

Frontend will run on:

```text
http://localhost:3000
```

---

## Backend Setup

```bash
cd backend

pip install -r requirements.txt
```

Run backend:

```bash
uvicorn main:app --reload
```

Backend will run on:

```text
http://localhost:8000
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
```

---

## 📦 Backend Requirements

Create `requirements.txt`

```txt
fastapi
uvicorn
python-dotenv
requests
groq
openai
networkx
pydantic
```

---

## 📦 Frontend Dependencies

```bash
npm install reactflow
npm install axios
npm install zustand
npm install react-icons
npm install react-router-dom
npm install uuid
npm install framer-motion
```

---

## 🧪 Example Workflow

### Input Node

```text
Artificial Intelligence in Healthcare
```

### Prompt Node

```text
Write a professional blog about {{input}}
```

### LLM Node

```text
Groq - Llama 3
```

### Output Node

```text
Generated Blog Content
```

---

## ⚙️ Workflow Execution Process

1. User creates workflow
2. Nodes are connected visually
3. Workflow validation runs
4. Variables are extracted
5. Prompt is generated
6. LLM executes request
7. Output node displays result
8. Logs are generated in execution console

---

## 🧩 Challenges Solved

### Dynamic Variable Replacement

```text
{{input}}
```

Dynamic placeholders are automatically resolved before execution.

### Workflow Validation

Prevented:

* Circular connections
* Invalid execution paths
* Missing dependencies

### Visual Node Management

Implemented:

* Drag & Drop nodes
* Dynamic node inspector
* Connection management
* Execution tracking

---

## 🔮 Future Improvements

* Multi-Agent Workflows
* RAG Integration
* Workflow Templates Marketplace
* Save & Load Workflows
* Authentication
* Team Collaboration
* Workflow Versioning
* Custom Node SDK

---

## 🎥 Demo

### Landing Page

Modern SaaS-inspired landing page with animated workflow visualizations.

### Builder

Visual node-based workflow editor built using React Flow.

### Execution Engine

FastAPI-powered backend execution engine with LLM integration.

---

## 👨‍💻 Author

**Manjunath R K**

AI/ML Engineer | Full Stack Developer

GitHub: https://github.com/manjunath9446

---

## 📄 License

MIT License

---

## 📝 Submission Notes

FlowCraft AI was built as a visual workflow orchestration platform inspired by modern AI workflow tools.

The project demonstrates:

* Visual workflow design
* Prompt engineering
* Variable management
* LLM integration
* Workflow validation
* Execution orchestration

through an intuitive drag-and-drop interface.
