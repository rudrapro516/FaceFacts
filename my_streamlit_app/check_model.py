from tensorflow.keras.models import load_model

# Load the best model
best_model = load_model('best_model.h5')

# Print the model summary
best_model.summary()
