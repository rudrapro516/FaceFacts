import streamlit as st

def patient_history():
    st.title("Patient History")
    st.write("Please enter your medical history below:")
    
    with st.form(key='history_form'):
        name = st.text_input("Patient Name")
        age = st.number_input("Age", min_value=0)
        medical_conditions = st.text_area("Medical Conditions")
        medications = st.text_area("Current Medications")
        allergies = st.text_area("Allergies")
        
        if st.form_submit_button("Submit"):
            st.success("Patient history submitted successfully!")