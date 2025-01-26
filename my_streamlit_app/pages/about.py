import streamlit as st

def about():
    st.title("About Us")
    st.write("At FaceFacts, we're here to help you better understand and care for your skin.")
    st.image("logo.jpg", caption="Our Mission")
    st.write("""
        We combine the latest in artificial intelligence with trusted dermatological knowledge 
        to create a tool that makes checking your skin simple, fast, and reliable.
    """)