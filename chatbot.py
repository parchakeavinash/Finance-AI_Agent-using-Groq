import streamlit as st
from groq import Groq

# Set API key explicitly
api_key = "GROQ_API_KEY"

if not api_key:
    st.error("API key not found! Please provide a valid API key.")
    st.stop()

# Initialize Groq client
client = Groq(api_key=api_key)

# Streamlit app UI
st.title("Chatbot using Streamlit and Groq")
st.write("Ask any question, and the bot will answer using the Groq API!")

# Chat input
user_input = st.text_input("Your message:", placeholder="Type your question here...")

if st.button("Send"):
    if user_input.strip():
        try:
            # Send request to Groq API
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ],
                model="llama3-8b-8192",
            )

            # Display the bot's response
            response = chat_completion.choices[0].message.content
            st.success(f"Bot: {response}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a message before clicking Send.")
