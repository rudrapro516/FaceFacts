import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model
import numpy as np

# Load the best model
best_model = load_model('best_model.h5')

# Define label classes
classes = {
    4: ('nv', 'melanocytic nevi'),
    6: ('mel', 'melanoma'),
    2: ('bkl', 'benign keratosis-like lesions'),
    1: ('bcc', 'basal cell carcinoma'),
    5: ('vasc', 'pyogenic granulomas and hemorrhage'),
    0: ('akiec', 'Actinic keratoses and intraepithelial carcinomae'),
    3: ('df', 'dermatofibroma')
}

def upload_image():
    st.title("Upload an Image for Classification")
    st.markdown('<div class="image-upload">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        if st.button("Analyze Image"):
            # Preprocess the image for the model
            image = image.resize((28, 28))  # Resize to the model's input size
            input_data = np.array(image) / 255.0  # Normalize the image
            input_data = np.expand_dims(input_data, axis=0)  # Add batch dimension
            
            # Make prediction
            prediction = best_model.predict(input_data)
            predicted_class_index = np.argmax(prediction)

            # Retrieve the corresponding label
            class_label = classes.get(predicted_class_index, ("unknown", "Unknown class"))
            st.write("Prediction result:", class_label[1])  # Display the class description

