FaceFacts: AI Doctor Web Application (Streamlit Version)
Overview

FaceFacts is a web application designed to assist users in understanding and managing their skin health. By leveraging artificial intelligence and dermatological knowledge, the application provides tools for symptom checking, health advice, patient history management, and more, built using Streamlit for a seamless user interface.
Features

    Symptom Checker: Users can describe their symptoms and receive insights into potential conditions.
    Health Advice: Access professional health advice tailored to individual needs.
    Patient History: Users can securely view and manage their medical history.
    Emergency Information: Quick access to emergency contact information and services.
    Camera Access: Users can capture and upload images for further analysis.

Technologies Used

    Frontend: Streamlit (Python)
    Backend: Python-based AI models (TensorFlow, Keras, etc.)
    Database: Local storage for patient history and captured images
    Styling: Custom CSS for responsive design

File Structure

MultipleFiles/
│
├── app.py                     # Streamlit application (main script)
├── symptoms_model.h5          # Pre-trained model for symptom analysis
├── image_processing.py        # Image processing logic
├── history_page.py            # Patient history page logic
├── about_page.py              # About us page logic
├── emergency_page.py          # Emergency services page logic
├── home_page.py               # Home page logic
├── advice_page.py             # Health advice page logic
├── camera_page.py             # Camera access page logic
└── assets/
    ├── home.css               # Custom CSS for styling
    └── logo.png               # Sample logo for the app

Installation

    Clone the repository:

git clone https://github.com/yourusername/FaceFacts.git

Navigate to the project directory:

cd FaceFacts/MultipleFiles

Install the necessary dependencies:

pip install -r requirements.txt

Run the application:

    streamlit run app.py

    Open your web browser and go to the URL provided by Streamlit (usually http://localhost:8501) to access the application.

Usage

    Launch the app by running the Streamlit script (streamlit run app.py).
    Navigate through the application using the provided sections (symptom checker, health advice, etc.).
    Use the symptom checker to describe your symptoms and get instant insights.
    View your patient history and emergency services information.
    Capture and upload images using the camera access feature for analysis.

Team Members
Laxit Jangid

    Role: Frontend Developer / UI/UX Designer
    Responsibilities: Laxit is responsible for creating and designing the frontend interface using Streamlit. He works on Streamlit's layout and design components to create a smooth, responsive, and user-friendly experience. He also integrates custom styling (CSS) and ensures that features like the symptom checker, camera access, and health advice are interactive and easy to use.
    Contact: +91 7878429752

Rudra Joshi

    Role: Backend Developer / AI Integration
    Responsibilities: Rudra handles the backend for the FaceFacts Streamlit app, focusing on the integration of AI models (like TensorFlow or Keras) for symptom checking and health advice. He also manages the image processing features and ensures smooth communication between the frontend and backend of the app. Rudra ensures that the user inputs (symptoms and images) are processed efficiently to provide accurate results.
    Contact: +91 9520144978

Contributing

Contributions are welcome! Please follow these steps:

    Fork the repository.
    Create a new branch:

git checkout -b feature-branch

Make your changes and commit them:

git commit -m 'Add new feature'

Push to the branch:

    git push origin feature-branch

    Create a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

    Thanks to the contributors and the open-source community for their support.
    Special thanks to the developers of Streamlit, TensorFlow, and Keras for their support in building the AI-based features.    
##FLOWCHART 
![screenshot][]
