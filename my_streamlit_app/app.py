import streamlit as st

# Import pages
from pages.home import home
from pages.about import about
from pages.contact import contact
from pages.symptoms import symptoms
from pages.upload_image import upload_image
from pages.emergency import emergency
from pages.health_advice import health_advice
from pages.patient_history import patient_history
from pages.chatbot import chatbot  # Import the chatbot
from pages.feedback import feedback  # Import the feedback functionality

from keras.models import load_model # type: ignore

# Load models
symptom_model = load_model('symptom_disease_model.h5')
best_model = load_model('best_model.h5')

def main():
    st.set_page_config(layout="wide")  # Set layout to wide

    if 'page' not in st.session_state:
        st.session_state.page = "Home"

    # Taskbar Navigation
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    with col1:
        if st.button("Home"):
            st.session_state.page = "Home"
    with col2:
        if st.button("About"):
            st.session_state.page = "About"
    with col3:
        if st.button("Contact"):
            st.session_state.page = "Contact"
    with col4:
        if st.button("Symptoms"):
            st.session_state.page = "Symptoms"
    with col5:
        if st.button("Upload Image"):
            st.session_state.page = "Upload Image"
    with col6:
        if st.button("Emergency"):
            st.session_state.page = "Emergency"
    with col7:
        if st.button("Health Advice"):
            st.session_state.page = "Health Advice"
    with col8:
        if st.button("Feedback"):  # Add button for feedback
            st.session_state.page = "Feedback"

    # Page Routing
    if st.session_state.page == "Home":
        home()
    elif st.session_state.page == "About":
        about()
    elif st.session_state.page == "Contact":
        contact()
    elif st.session_state.page == "Symptoms":
        symptoms()
    elif st.session_state.page == "Upload Image":
        upload_image()
    elif st.session_state.page == "Emergency":
        emergency()
    elif st.session_state.page == "Health Advice":
        health_advice()
    elif st.session_state.page == "Feedback":  # Route to feedback
        feedback()

    # Chatbot Icon
    st.sidebar.image("chatbot icon.png", width=50)  # Add your chatbot icon path here
    if st.sidebar.button("Chat with us"):
        st.session_state.page = "Chatbot"

    # Footer
    st.markdown('<div class="footer">', unsafe_allow_html=True)
    st.write("© 2023 FaceFacts. All rights reserved.")
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
