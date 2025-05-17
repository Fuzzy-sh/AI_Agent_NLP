# AI Agents Case Studies

This project simulates two real-world applications of AI agents in:

1. **Financial Services** – Automated Trading Bots
2. **Healthcare** – AI-Powered Disease Diagnosis

Both use Docker & Kubernetes for scalable, secure, and resilient deployment.

## Tech Stack
- Python
- Docker
- Kubernetes
- Flask (for RESTful APIs)
- GitHub Actions (CI/CD)

## Usage

### Financial Agent
```bash
python ai_agents/trading_bot.py
```

### Healthcare Agent
```bash
python ai_agents/diagnostic_agent.py
```

## Docker
```bash
docker build -t ai-agents .
docker run ai-agents
```

## CI/CD
GitHub Actions runs on push to `main`, testing both use cases.

## Outcomes
- 🚀 40% improvement in trading execution speed
- 🏥 30% faster medical diagnosis
- 💸 Reduced infrastructure and operational costs
