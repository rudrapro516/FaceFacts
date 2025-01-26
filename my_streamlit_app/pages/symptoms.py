import streamlit as st
import numpy as np
from pages.api_integration import get_health_data  # Import the API integration function

# Updated disease names corresponding to model output
disease_names = [
    "Acne", "Arthritis", "Bronchial Asthma", "Cervical spondylosis", "Chicken pox",
    "Common Cold", "Dengue", "Dimorphic Hemorrhoids", "Fungal infection", "Hypertension",
    "Impetigo", "Jaundice", "Malaria", "Migraine", "Pneumonia", "Psoriasis", "Typhoid",
    "Varicose Veins", "Allergy", "Diabetes", "Drug reaction",
    "Gastroesophageal reflux disease", "Peptic ulcer disease", "Urinary tract infection"
]

def symptoms():
    st.title("Describe Symptoms")
    symptoms_list = [
        "Fever", "Skin Rash/Lesions", "Joint Pain", "Headache", "Fatigue",
        "Cough", "Difficulty Breathing", "Itching", "Stomach Pain",
        "Nausea/Vomiting", "Muscle Pain", "Swelling", "Neck/Back Stiffness",
        "Yellowish Skin", "Burning Urination",
        "Skin rash on arms, legs, and torso", "Red, itchy, dry, scaly patches",
        "Peeling skin on knees, elbows, and scalp", "Burning or stinging sensation",
        "Joint pain in fingers, wrists, and knees", "Silver-like dusting on skin",
        "Small dents or pits in nails", "Thickened skin on palms and soles with deep cracks",
        "Red and inflamed skin around mouth, nose, and eyes",
        "Sensitive skin reacting to temperature or humidity changes",
        "Sudden peeling of skin", "Red and inflamed skin on genitals",
        "Fatigue and malaise", "Rash spreading to chest and abdomen",
        "Rash worse in winter months", "Difficulty sleeping due to itching",
        "Prone to infections due to dry patches"
    ]

    selected_symptoms = st.multiselect("Select Symptoms", symptoms_list)
    if st.button("Analyze"):
        st.write("Analyzing symptoms:", selected_symptoms)
        
        # Convert selected symptoms to model input format
        input_data = np.zeros((1, 1444))  # Adjusted to match expected input shape
        for symptom in selected_symptoms:
            if symptom in symptoms_list:
                input_data[0, symptoms_list.index(symptom)] = 1
        
        # Debugging: Print input data shape and content
        st.write("Input data shape:", input_data.shape)
        st.write("Input data content:", input_data)

        # Placeholder for prediction logic
        # Here you can implement an alternative method for making predictions
        # For example, using a different model or a set of rules
        # prediction = alternative_prediction_method(input_data)

        # Display a placeholder result
        st.write("Predicted Disease: [Placeholder for prediction]")

        # Provide personalized health tips based on the predicted disease
        recommendations = {
            "Acne": "Consider using topical treatments and maintaining a good skincare routine.",
            "Arthritis": "Consult a rheumatologist for appropriate management and treatment options.",
            "Bronchial Asthma": "Ensure you have an inhaler and avoid known triggers.",
            "Cervical spondylosis": "Physical therapy and pain management strategies may help.",
            "Chicken pox": "Stay hydrated and consult a doctor for antiviral medications.",
            "Common Cold": "Rest, stay hydrated, and consider over-the-counter medications.",
            "Dengue": "Seek medical attention for monitoring and supportive care.",
            "Dimorphic Hemorrhoids": "Consider dietary changes and topical treatments.",
            "Fungal infection": "Antifungal creams or medications may be necessary.",
            "Hypertension": "Monitor your blood pressure and consult a healthcare provider.",
            "Impetigo": "Antibiotic treatment is usually required.",
            "Jaundice": "Seek medical evaluation for underlying liver issues.",
            "Malaria": "Consult a healthcare provider for antimalarial medications.",
            "Migraine": "Consider lifestyle changes and consult a doctor for medication.",
            "Pneumonia": "Seek medical attention for appropriate antibiotics.",
            "Psoriasis": "Topical treatments and lifestyle changes may help manage symptoms.",
            "Typhoid": "Consult a healthcare provider for antibiotics.",
            "Varicose Veins": "Consider compression stockings and consult a doctor.",
            "Allergy": "Identify and avoid allergens; antihistamines may help.",
            "Diabetes": "Monitor blood sugar levels and consult a healthcare provider.",
            "Drug reaction": "Seek immediate medical attention if severe.",
            "Gastroesophageal reflux disease": "Consider dietary changes and medications.",
            "Peptic ulcer disease": "Consult a healthcare provider for treatment options.",
            "Urinary tract infection": "Antibiotics are usually required; stay hydrated."
        }

        st.write("Recommendations:", recommendations.get("[Placeholder for prediction]", "No specific recommendations available."))

        # Fetch and display health data from the API
        health_data = get_health_data("[Placeholder for prediction]")
        st.write("Health Data:", health_data)
