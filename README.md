# Google ADK Agents

A collection of AI agents built using the Google Agent Development Kit (ADK), demonstrating various agent architectures and interaction patterns.

## 🔍 Overview

This project showcases different types of AI agent implementations using Google's ADK framework and Gemini models. It includes four distinct agent patterns:

- **Single Agent**: A straightforward conversational agent for general-purpose interactions
- **Multi-Agent Sequential**: Agents that process tasks in a sequential workflow
- **Multi-Agent Parallel**: Agents that work simultaneously on different aspects of a problem
- **Multi-Agent Loop**: Agents that operate in iterative cycles for complex problem-solving

## 🚀 Use Cases

This project is ideal for:

- **Learning AI Agent Development**: Understand different agent architectures and patterns
- **Prototyping Conversational AI**: Quick setup for testing AI assistant capabilities
- **Building Multi-Agent Systems**: Explore collaborative AI workflows for complex tasks
- **Educational Purposes**: Teach concepts of distributed AI and agent coordination
- **Customer Support Solutions**: Deploy intelligent assistants for user queries
- **Content Generation**: Leverage multiple agents for creative and analytical tasks

## 📋 Prerequisites

- Python 3.13 or higher
- Google API key for Gemini models
- [uv](https://github.com/astral-sh/uv) package manager

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd agents
   ```

2. **Install dependencies using uv**:
   ```bash
   uv sync
   ```
   
   This will automatically:
   - Create a virtual environment
   - Install all dependencies from `pyproject.toml`
   - Set up the Google ADK framework

3. **Set up environment variables**:
   
   Each agent directory contains a `.env` file. Update them with your Google API key:
   ```bash
   # In each agent's .env file
   GOOGLE_GENAI_USE_VERTEXAI=0
   GOOGLE_API_KEY=your_google_api_key_here
   ```

   To get a Google API key:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy and paste it into the `.env` files

## 🏃‍♂️ Usage

### Running the Web Interface

Start the ADK web server to interact with all agents through a browser interface:

```bash
uv run adk web
```

This will:
- Start a web server on `http://127.0.0.1:8000`
- Automatically discover and load all agent configurations
- Provide a user-friendly interface to chat with each agent

### Available Agents

1. **single_agent**: Basic conversational assistant
2. **multi_agent_sequential**: Sequential task processing
3. **multi_agent_parallel**: Parallel task execution
4. **multi_agent_loop**: Iterative problem solving

### Command Line Usage

You can also run individual agents programmatically by importing them:

```python
from single_agent.agent import root_agent
# Use the agent in your code
```

## 📦 Dependencies

- **google-adk**: Core Google Agent Development Kit framework (>=1.19.0)
- **Python 3.13**: Required for latest language features and compatibility

All dependencies are managed through `pyproject.toml` and automatically installed via `uv sync`.

## 🔧 Development

### Project Structure

```
agents/
├── pyproject.toml          # Project configuration and dependencies
├── README.md              # This file
├── single_agent/          # Basic conversational agent
├── multi_agent_sequential/# Sequential workflow agents
├── multi_agent_parallel/  # Parallel processing agents
└── multi_agent_loop/      # Iterative processing agents
```

### Adding New Agents

1. Create a new directory for your agent
2. Add `__init__.py` and `agent.py` files
3. Create a `.env` file with your API configuration
4. Define your agent using the Google ADK Agent class

### Running in Development Mode

The web interface automatically reloads when you make changes to agent files, making development iteration fast and efficient.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with `uv run adk web`
5. Submit a pull request

## 📄 License

This project is open source. Please check the license file for details.

## 🆘 Troubleshooting

### Common Issues

- **API Key Errors**: Ensure your Google API key is valid and has Gemini API access enabled
- **Port Conflicts**: The web server runs on port 8000 by default. Ensure it's available
- **Python Version**: Make sure you're using Python 3.13 or higher

### Getting Help

- Check the [Google ADK Documentation](https://developers.google.com/adk)
- Review agent logs in the web interface
- Ensure all `.env` files are properly configured

## 🌟 Next Steps

After getting the basic setup running, consider:

- Customizing agent instructions and behaviors
- Adding tools and functions to agents
- Implementing custom multi-agent workflows
- Integrating with external APIs and services
- Deploying agents to production environments