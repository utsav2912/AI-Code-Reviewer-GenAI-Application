import streamlit as st
import google.generativeai as genai
import apikey

# Configure API key
genai.configure(api_key=apikey.GOOGLE_API_KEY)

# Load the Gemini model
llm = genai.GenerativeModel("models/gemini-1.5-flash")

# Initialize the chatbot
chatbot = llm.start_chat(history=[])

# Streamlit app title
st.title("AI Code Reviewer")

# Initial AI message
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "ai", "content": "Hi there! I'm your AI code reviewer. Paste your Python code below and I'll provide feedback."}
    ]

# Display chat messages
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# User input
human_prompt = st.chat_input("Paste your Python code here:", key="unique_key")

if human_prompt:
    # Display the user's message
    st.chat_message("human").write(f"```python\n{human_prompt}\n```")
    st.session_state.messages.append({"role": "human", "content": human_prompt})

    # AI response
    try:
        review_prompt = f"Review the following Python code and provide feedback on potential issues, improvements, and suggestions for refactoring:\n```python\n{human_prompt}\n```"
        response = chatbot.send_message(review_prompt)
        response_text = response.text if hasattr(response, 'text') else response['text']
        st.chat_message("ai").write(response_text)
        st.session_state.messages.append({"role": "ai", "content": response_text})
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        st.chat_message("ai").write(error_message)
        st.session_state.messages.append({"role": "ai", "content": error_message})