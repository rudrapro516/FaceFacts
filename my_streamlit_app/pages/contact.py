import streamlit as st

def contact():
    st.title("Contact Us")
    st.write("Our Information")
    st.write("Name: Laxit Jangid, Contact No: +91 7878429752")
    st.write("Name: Rudra Joshi, Contact No: +91 9520144978")
    
    with st.form(key='contact_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        contact_no = st.text_input("Contact No")
        message = st.text_area("Message")
        if st.form_submit_button("Submit"):
            st.success("Form submitted successfully!")