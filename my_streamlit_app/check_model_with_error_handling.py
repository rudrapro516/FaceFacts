from tensorflow.keras.models import load_model

try:
    # Load the best model
    best_model = load_model('best_model.h5')
    # Print the model summary
    best_model.summary()
except Exception as e:
    print("Error loading the model:", e)
