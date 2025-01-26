import streamlit as st

def health_advice():
    st.title("Health Advice")
    st.write("Here are some tips for maintaining good health:")
    advice_list = [
        "Stay hydrated by drinking plenty of water.",
        "Eat a balanced diet rich in fruits and vegetables.",
        "Engage in regular physical activity.",
        "Get enough sleep each night.",
        "Manage stress through mindfulness and relaxation techniques."
    ]
    for advice in advice_list:
        st.write(f"- {advice}")