import os
import streamlit as st
from dotenv import load_dotenv
from interview_bot import InterviewBot
from prompts import SYSTEM_PROMPT, TECH_PROMPT_FIRST, TECH_PROMPT_FOLLOWUP

# Load .env file for API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("⚠️ Please set GEMINI_API_KEY in your .env file")
    st.stop()

# Initialize bot in Streamlit session state
if "bot" not in st.session_state:
    st.session_state.bot = InterviewBot(
        SYSTEM_PROMPT,
        TECH_PROMPT_FIRST,
        TECH_PROMPT_FOLLOWUP,
        api_key
    )
    st.session_state.history = []
    st.session_state.start_msg = st.session_state.bot.start()

st.set_page_config(page_title="TalentScout - Hiring Assistant", page_icon="🤖")

st.title("🤖 TalentScout - AI Hiring Assistant")

# Display initial bot message
if st.session_state.start_msg and not st.session_state.history:
    st.chat_message("assistant").write(st.session_state.start_msg)

# Chat input for user
if prompt := st.chat_input("Type your response..."):
    st.chat_message("user").write(prompt)
    st.session_state.history.append(("user", prompt))

    response = st.session_state.bot.step(prompt)

    # Save last response in session_state
    st.session_state.last_response = response

    st.chat_message("assistant").write(response)
    st.session_state.history.append(("assistant", response))

# ✅ Check interview completion outside chat block
if "last_response" in st.session_state and "Thank you for your time" in st.session_state.last_response:
    st.success("✅ Interview complete! Candidate data has been saved.")

    if st.button("🔄 Start Another Interview"):
        st.session_state.bot = InterviewBot(
            SYSTEM_PROMPT,
            TECH_PROMPT_FIRST,
            TECH_PROMPT_FOLLOWUP,
            api_key
        )
        st.session_state.history = []
        st.session_state.start_msg = st.session_state.bot.start()
        del st.session_state.last_response
        st.rerun()
