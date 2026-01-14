import streamlit as st
import re
import os 
from dotenv import load_dotenv 
from agents import get_pro_agent, get_con_agent, get_judge_agent

load_dotenv()

# 1. Page Config (Wide mode is still best for 3 columns)
st.set_page_config(page_title="AI Debate Arena", page_icon="🗣️", layout="wide")

# 2. Session State Initialization
if 'debate_history' not in st.session_state:
    st.session_state.debate_history = []
if 'topic' not in st.session_state:
    st.session_state.topic = ""

# 3. Helper for cleaning <think> tags
def clean_text(text):
    if not text:
        return ""
    # Removes reasoning blocks and empty tags
    cleaned = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    return cleaned.strip()

# --- UI HEADER ---
st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="margin-bottom: 0;">🗣️ AI Debate Arena</h1>
        <p style="font-size: 1.2rem; color: #808495; margin-top: 0;">A multi-agent battle powered by Agno and Groq</p>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("")

# Topic Input
topic_input = st.text_input("Enter Debate Topic:", value="AI will eventually replace human programmers")

# Action Buttons
col_btn1, col_btn2, _ = st.columns([1, 1, 4])
with col_btn1:
    if st.button("🚀 Start Round", use_container_width=True):
        st.session_state.topic = topic_input
        
        # Initialize Agents
        pro_a = get_pro_agent()
        con_a = get_con_agent()
        judge_a = get_judge_agent()
        
        with st.status("Agents are debating...", expanded=True) as status:
            st.write("Pro Agent is formulating argument...")
            p_res = clean_text(pro_a.run(f"Topic: {st.session_state.topic}").content)
            
            st.write("Con Agent is preparing rebuttal...")
            c_res = clean_text(con_a.run(f"Rebut this: {p_res}").content)
            
            st.write("Judge is evaluating...")
            j_res = clean_text(judge_a.run(f"Judge this debate: \nPro Agent: {p_res}\nCon Agent: {c_res}").content)
            
            status.update(label="Debate Round Complete!", state="complete", expanded=False)
            
            # Save to History
            st.session_state.debate_history.append({
                "round": len(st.session_state.debate_history) + 1,
                "pro": p_res,
                "con": c_res,
                "judge": j_res
            })

with col_btn2:
    if st.button("🗑️ Reset", use_container_width=True):
        st.session_state.debate_history = []
        st.rerun()

st.divider()

# --- DISPLAY DEBATE HISTORY ---
if st.session_state.debate_history:
    # Show newest rounds at the top
    for turn in reversed(st.session_state.debate_history):
        round_label = f"Round #{turn['round']}"
        
        # Using Streamlit Expanders for history
        with st.expander(round_label, expanded=(turn['round'] == len(st.session_state.debate_history))):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.subheader("🟢 Pro Agent")
                # Native border container automatically handles theme colors
                with st.container(border=True):
                    st.markdown(turn["pro"])
            
            with col2:
                st.subheader("🔴 Con Agent")
                with st.container(border=True):
                    st.markdown(turn["con"])
                
            with col3:
                st.subheader("⚖️ Judge")
                with st.container(border=True):
                    # success() gives a nice green background for the winner
                    st.info(turn["judge"])
else:
    st.info("Enter a topic and click 'Start Round' to see the agents in action.")