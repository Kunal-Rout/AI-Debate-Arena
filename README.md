# 🗣️ AI Debate Arena

An interactive, multi-agent debate platform where AI agents battle it out on any topic, overseen by an impartial AI judge. Built with **Streamlit**, **Agno**, and **Groq**.

## 🚀 Features
- **Pro & Con Agents:** Powered by `Llama-3.3-70b` for high-speed, logical arguments.
- **AI Judge:** Powered by `Qwen-32b` for decisive and structured evaluation.
- **Native UI:** Clean, centered Streamlit interface that supports Light and Dark modes.
- **History Tracking:** View previous rounds in organized expanders.

## 🛠️ Tech Stack
- **Framework:** [Agno](https://www.agno.com/) (Agentic Workflows)
- **Frontend:** [Streamlit](https://streamlit.io/)
- **Inference:** [Groq Cloud](https://groq.com/) (Ultra-fast LLM responses)

## 💡 Inspiration
This project was inspired by a similar debate concept built with LangGraph. I chose to rebuild it using **Agno** to explore streamlined multi-agent orchestration and low-latency inference.

## 🏃 How to Run
1. Clone the repo
2. Create a `.env` file with your `GROQ_API_KEY`
3. Install dependencies: `pip install streamlit agno python-dotenv`
4. Run the app: `streamlit run app.py`