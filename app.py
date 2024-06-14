from flask import Flask, request, jsonify
import pickle
import os
import os.path
import time
import pandas as pd

docker_image_tag = os.environ.get('IMAGE_VERSION', 'Unknown')

app = Flask(__name__)

@app.route("/api/recommender", methods=["POST"])

def recommend_api():
    try:
        input_json = request.get_json()
        input_songs = input_json['songs']

        app.rules = pickle.load(open("/ml/rules.pickle", "rb"))
        model_date = time.ctime(os.path.getmtime("/ml/rules.pickle"))

        recommended = set()
        for _, row in app.rules.iterrows():
            if any(x in row['antecedents'] for x in input_songs):
                for x in row['consequents']:
                    recommended.add(x)
    
        recommended -= set(input_songs)
    
        return jsonify({
            'songs': list(recommended),
            'version': docker_image_tag,
            'model_date': model_date
        })

    except Exception as e:
        return jsonify({'error': str(e)})
