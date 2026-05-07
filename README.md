# ADK Hackathon Demo 🚀

Welcome to the simplified ADK Hackathon Demo! This repository contains a clean, organized agent built using the **Agent Development Kit (ADK)**.

## 📂 Project Structure

- `demo-agent/`: The main demo directory.
  - `deploy.py`: A simple script to deploy your agent to **Vertex AI Agent Engine**.
  - `agent/`: The core agent code.
    - `agent.py`: The entry point for your agent. Defines the `root_agent` and the `App`.
    - `sub_agent.py`: Demonstrates how to create a specialized sub-agent for delegation.
    - `tools.py`: A collection of Python functions that your agents can use as tools.
    - `requirements.txt`: List of dependencies needed for deployment.

## 🛠️ Getting Started

### 1. Prerequisites
- Python 3.10+
- `adk` installed (`pip install google-agents-cli`)

### 2. Environment Setup
Create a `.env` file in the root or `demo-agent` directory with your Google Cloud project details:
```bash
GOOGLE_CLOUD_PROJECT=YOUR PROJECT ID
GOOGLE_CLOUD_LOCATION=us-central1
GOOGLE_GENAI_USE_VERTEXAI=1
```

If you cannot find your .env file to update, you may need to click view -> toggle hidden files.
Once updated you can toggle to hide the folders again.

### 3. Setup & Local Testing
Navigate to the `demo-agent` directory, install dependencies, and run the local playground:
```bash
cd demo-agent
pip install -r agent/requirements.txt
adk web agent/
```

### 3. Deploy to Agent Engine
When you're ready to share your agent with the world, run the following command from the `demo-agent` directory:

```bash
cd demo-agent
adk deploy agent_engine agent/ --project=YOUR_PROJECT_ID --region=YOUR_REGION
```
*Example with project: `--project=dev-australia-xyz-gazo-0`* You will need to replace 0 with your project number.
*Example with region: `--region=us-central1`*

Note: Ensure you have your Google Cloud project set up and you are authenticated (`gcloud auth login`).

## 🧠 Learning & Development

This repository includes **ADK Skills** (located in `.agents/skills/`) which provide interactive documentation and code patterns for your AI coding assistant. You can ask your assistant (like Antigravity or Cursor) to refer to these files:

- **ADK Workflow**: Full lifecycle guide from scaffolding to deployment.
- **ADK Code Patterns**: Cheatsheet for agents, tools, and state management.
- **Project Scaffolding**: How to use `agents-cli scaffold` to enhance your project.
- **Google Docs Skill**: Access to authoritative Google Developer documentation.

## 🚀 How to Improve This Agent

1. **Add More Tools**: Open `agent/tools.py` and add a new function. Then register it in `agent/agent.py` or `agent/sub_agent.py`.
2. **Refine Instructions**: Change the `instruction` strings in the agent files to give them different personalities.
3. **Complex Workflows**: Add more sub-agents and see how the Root Agent handles delegation.

Happy Hacking! 🛠️✨