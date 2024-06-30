from flask import Flask, request, jsonify
import onnxruntime as ort
import numpy as np

app = Flask(__name__)

@app.route("/api/predict", methods=["POST"])

def predict_api():
    try:
        model_path = 'model0.onnx'
        session = ort.InferenceSession(model_path)

        input_json = request.get_json()
        batch_size = input_json['batch_size']
        input_tensor = np.random.rand(batch_size, 3, 64, 64).astype(np.float32)

        input_name = session.get_inputs()[0].name
        output_name = session.get_outputs()[0].name

        outputs = session.run([output_name], {input_name: input_tensor})

        return jsonify({'result': outputs[0].tolist()})

    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)