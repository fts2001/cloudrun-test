from flask import Flask, request, jsonify
import torch

app = Flask(__name__)

@app.route("/api/predict", methods=["POST"])

def predict_api():
    try:
        input_json = request.get_json()

        model = torch.load('simple_model_full.pth')
        model.eval()

        input_data = torch.tensor(input_json['data'])
        output = model(input_data)
        return jsonify({'result': output.item()})

    except Exception as e:
        return jsonify({'error': str(e)})
