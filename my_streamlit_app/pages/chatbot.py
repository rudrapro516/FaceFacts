import streamlit as st
import requests

def chatbot():
    st.title("Health Chatbot")
    user_input = st.text_input("Ask me anything about your symptoms or health concerns:")

    if st.button("Send"):
        response = generate_response(user_input)
        st.write("Chatbot:", response)

def generate_response(user_input):
    # Integrate Gemini API for generating responses
    api_url = "https://api.gemini.ai/v1/chat"  # Replace with actual Gemini API endpoint
    headers = {
        "Authorization": "Bearer AIzaSyBcViJTQPW6iFTgm-lWy7jupWiEi7exdCc",  # Use provided Gemini API key
        "Content-Type": "application/json"
    }
    payload = {
        "message": user_input
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)  # Added commas
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data.get("response", "I'm not sure about that. Please consult a healthcare professional for accurate advice.")  # Added comma
    except requests.exceptions.RequestException as e:
        return f"Error fetching response: {str(e)}"
