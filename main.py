# from flask import Flask, request, jsonify
import torch

# app = Flask(__name__)

# Load the Faiss index from the pickle file
with open('faiss_index.pkl', 'rb') as f:
    model = torch.load(f, map_location=torch.device('cpu'))

# @app.route('/api/predict', methods=['POST'])
# def predict():
#     data = request.get_json()
#     input_data = data['inputData']

#     # Make predictions
#     # Example: prediction = model.similarity_search(input_data)
    
#     # Return the prediction as JSON response
#     return jsonify({'prediction': 'Placeholder prediction'})

# if __name__ == '__main__':
#     app.run(debug=True)
    query = "who is going to play instead of virat"
docs = model.similarity_search(query)
print(docs)
