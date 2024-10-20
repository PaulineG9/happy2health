import streamlit as st
from chatbot import chatbot_response  # Import chatbot logic

st.title("Chat with our Support Bot")

user_input = st.text_input("Type your message:")
if st.button("Send"):
    response = chatbot_response(user_input)
    st.write(response)
