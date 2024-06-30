from flask import Flask, request, jsonify
import torch
import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(5, 1)
    
    def forward(self, x):
        return self.fc(x)

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
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)