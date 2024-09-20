# import requests

# def emotion_detector(text_to_analyse):
#     URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
#     headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#     input_json = { "raw_document": { "text": text_to_analyse } }
#     response = requests.post(URL, json = input_json, headers=headers)  
#     return response.text

# import json

# data = '{"emotionPredictions":[{"emotion":{"anger":0.01364663, "disgust":0.0017160787, "fear":0.008986978, "joy":0.9719017, "sadness":0.055187024}, "target":"", "emotionMentions":[{"span":{"begin":0, "end":27, "text":"I love this new technology."}, "emotion":{"anger":0.01364663, "disgust":0.0017160787, "fear":0.008986978, "joy":0.9719017, "sadness":0.055187024}}]}], "producerId":{"name":"Ensemble Aggregated Emotion Workflow", "version":"0.0.1"}}'
# data = json.loads(data)
# print(data["emotionPredictions"][0]["emotion"])

 
data = {'anger': 0.01364663, 'disgust': 0.0017160787, 'fear': 0.008986978, 'joy': 0.9719017, 'sadness': 0.055187024}

temp_score = 0
dominant_emotion = None
for key, value in data.items():
    if temp_score < value:
        temp_score = value
        dominant_emotion = key

data["dominant_emotion"] = dominant_emotion

print(data)