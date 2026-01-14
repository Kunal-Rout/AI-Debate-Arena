import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq

load_dotenv()

# Agent 1: Pro Agent
def get_pro_agent():
    return Agent(
        name="Pro-Debater",
        role="Argue strongly in FAVOR of the topic",
        # Added api_key here
        model=Groq(id="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY")),
        instructions=[
            "Provide a strong, persuasive argument.",
            "STRICT LIMIT: Keep your response under 200 words.", 
            "Use 5 clear bullet points for your main arguments.",
            "Be firm and use impactful language."
        ],
        markdown=True
    )

# Agent 2: Con Agent
def get_con_agent():
    return Agent(
        name="Con-Debater",
        role="Argue strongly AGAINST the topic",
        model=Groq(id="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY")),
        instructions=[
            "Identify flaws in the proponent's logic.",
            "STRICT LIMIT: Keep your response under 200 words.", 
            "Address specific points mentioned by the opponent.",
            "Provide a logical counter-argument."
        ],
        markdown=True
    )

# Agent 3: The Judge
def get_judge_agent():
    return Agent(
        name="The Judge",
        role="A detailed and decisive debate judge",
        # Added api_key here
        model=Groq(id="qwen/qwen3-32b", api_key=os.getenv("GROQ_API_KEY")),
        instructions=[
            "Provide a balanced evaluation of both sides.",
            "Length: Aim for about 100-150 words (more detailed than before).",
            "Use this structure:",
            "### 📊 Scorecard",
            "**Pro Agent:** X/10 | **Con Agent:** Y/10",
            "### 🔍 Analysis",
            "Explain specifically what made one side more convincing than the other.",
            "### 🏆 FINAL VERDICT",
            "State the winner in bold."
        ],
        markdown=True
    )