# Multi-AI-Agent-for-financial-and-web-search

AI-FinAgent is a modular, multi-agent AI system designed to conduct intelligent financial analysis and live web search through autonomous collaboration. Built with the PHI agent framework and powered by Groq LLM, it provides real-time stock insights, news summaries, and data-driven decisions via an interactive AI playground.

---

## 🚀 Key Features

✅ Multi-agent architecture using the PHI framework

✅ Real-time web search via DuckDuckGo API

✅ Stock data and financial metrics via Yahoo Finance (finance)

✅ Groq LLM-powered reasoning and response generation

✅ Deployed interactive web-based AI playground for user queries and insights

---

## 🧠 Architecture Overview

* 🔧 PHI agents collaborate asynchronously to divide and complete subtasks:

  * WebAgent: Queries and summarizes recent web data.
  * FinanceAgent: Analyzes stocks and retrieves financial KPIs.
  * AnalystAgent: Synthesizes findings using Groq LLM.

* 🌐 Real-time Tools Integrated:

  * DuckDuckGo Search API
  * yfinance Python library

* 🖥️ Frontend: Simple AI playground (Streamlit or Flask)

---

## 🔍 Use Cases

* 💹 Query “What’s the latest analysis of AAPL stock?”
* 📰 Ask “Summarize the current news around inflation.”
* 📊 Compare “Which company had better Q1 revenue: TSLA or NVDA?”

---

## 🧰 Tech Stack

| Component       | Tool/Library      |
| --------------- | ----------------- |
| Agent Framework | PHI               |
| Web Search      | DuckDuckGo API    |
| Financial Data  | yfinance          |
| LLM Backend     | Groq LLM (Cloud)  |
| Deployment      | Streamlit / Flask |

---

## 📁 Project Structure

```
AI-FinAgent/
│
├── financial_agent.py                 # API keys, Groq integration
├── playground.py                  # Entry point
├── requirements.txt
└── README.md
```

---

## 🧪 Installation

1. Clone the repo:

```bash
git clone https://github.com/Al-Shafi-Github/Multi-AI-Agent-for-financial-and-web-search.git

```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set API keys (Groq, DuckDuckGo, etc.) in config/.env or directly in config.py.

4. Launch the AI Playground:

```bash
python playground.py
```

or



---

## 📝 Example Interaction

> User: “Should I invest in Google right now?”
>
> 🤖 WebAgent: “Recent headlines include Google’s Gemini 1.5 release and strong Q2 earnings.”
> 🤖 FinanceAgent: “GOOGL current price is \$138.40. P/E: 22.34. EPS: 6.48.”
> 🤖 AnalystAgent: “Based on current valuation and sentiment, GOOGL appears fairly priced with moderate upside potential.”

---

## 🔒 Security & Privacy

* Only public search and financial data are retrieved.
* No user data is stored or logged.


