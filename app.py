# Import necessary libraries
from flask import Flask, request, jsonify
import joblib

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model and TF-IDF vectorizer
# These must be the same files created during training
model = joblib.load('fake_news_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Root route: simple message to confirm the API is running
@app.route('/')
def home():
    return "✅ Fake News Detection API is running."

# Prediction route: accepts POST requests with news text
@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request body
    data = request.get_json()

    # Validate input
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing \"text\" field in JSON request'}), 400

    # Extract the input text
    input_text = data['text']

    # Vectorize the input text using the same vectorizer used during training
    vectorized_input = vectorizer.transform([input_text])

    # Make prediction: 1 = REAL, 0 = FAKE
    prediction = model.predict(vectorized_input)[0]
    label = "REAL" if prediction == 1 else "FAKE"

    # Return the prediction as JSON
    return jsonify({'prediction': label})

# Start the Flask app (only runs locally unless deployed)
if __name__ == '__main__':
    # Debug mode is useful during development but should be turned off in production
    app.run(debug=True)
