import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Business Assistant")

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.title("AI Business Assistant")
st.write("This is a demo AI assistant powered by Google Gemini.")

user_input = st.text_area("Ask a business-related question:")

if st.button("Ask AI"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)
        st.success("AI Response:")
        st.write(response.text)
