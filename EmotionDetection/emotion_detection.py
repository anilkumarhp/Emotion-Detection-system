import requests
import json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = input_json, headers=headers)  
    if response.status_code == 200:
        data = json.loads(response.text)
        data = data["emotionPredictions"][0]["emotion"]
        temp_score = 0
        dominant_emotion = None
        for key, value in data.items():
            if temp_score < value:
                temp_score = value
                dominant_emotion = key

        data["dominant_emotion"] = dominant_emotion
        return data
    elif response.status_code == 400:
        data = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
        return data
