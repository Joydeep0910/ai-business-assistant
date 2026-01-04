import streamlit as st
import google.generativeai as genai
import os

# Configure the Gemini API key from environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="AI Business Assistant")

st.title("AI Business Assistant - Hosted on PartyRock")
st.write("This is a demo AI assistant that can answer business questions.")

# Default prompt
default_prompt = """
You are an AI business assistant.
Help company employees and customers by providing clear, concise, and professional responses.
You can summarize documents, answer questions, provide advice, and generate polite replies.
Always be professional.
"""

# User input
user_input = st.text_area("Ask a business question:", default_prompt)

# Button to get AI response
if st.button("Ask AI"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        model = genai.GenerativeModel("text-bison-001")  # Free-tier model
        response = model.generate_content(user_input)
        st.success("AI Response:")
        st.write(response.text)
