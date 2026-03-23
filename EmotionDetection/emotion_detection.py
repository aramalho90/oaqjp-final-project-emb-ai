import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { 
            "raw_document": { "text": text_to_analyse } 
            }

    response = requests.post(url, headers = header, json = data)

    response_dict = '{ "anger": 0, "disgust": 0, "fear": 0, "joy": 0, "sadness": 0, "dominant_emotion": 0 }'
    response_dict = json.loads(response_dict)

    response_dict['anger'] = response.json()['emotionPredictions'][0]['emotion']['anger']
    response_dict['disgust'] = response.json()['emotionPredictions'][0]['emotion']['disgust']
    response_dict['fear'] = response.json()['emotionPredictions'][0]['emotion']['fear']
    response_dict['joy'] = response.json()['emotionPredictions'][0]['emotion']['joy']
    response_dict['sadness'] = response.json()['emotionPredictions'][0]['emotion']['sadness']

    max_key = max(response_dict, key=response_dict.get)
    response_dict['dominant_emotion'] = max_key

    return response_dict