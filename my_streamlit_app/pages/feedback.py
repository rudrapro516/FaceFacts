import streamlit as st

def feedback():
    st.title("User Feedback")
    st.write("We value your feedback! Please let us know how helpful the recommendations were.")
    
    feedback_options = ["Very Helpful", "Helpful", "Neutral", "Not Helpful", "Very Not Helpful"]
    selected_feedback = st.selectbox("How helpful were the recommendations?", feedback_options)
    
    comments = st.text_area("Additional Comments:")
    
    if st.button("Submit Feedback"):
        # Here you would typically save the feedback to a database or file
        st.success("Thank you for your feedback!")
        # For demonstration, we can print the feedback to the console
        print(f"Feedback: {selected_feedback}, Comments: {comments}")
