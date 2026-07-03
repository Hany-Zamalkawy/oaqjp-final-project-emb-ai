import requests
import json

def emotion_detector(text_to_analyze):
    # The Watson NLP emotion prediction endpoint (running in your lab's Docker container)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # The payload Watson expects: your text wrapped in a "raw_document" object
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Header tells Watson which model to use
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send the POST request
    response = requests.post(url, json=myobj, headers=header)

    # Convert the JSON string response into a Python dictionary
    formatted_response = json.loads(response.text)

    # Drill into the nested structure to get the emotion scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    # Find which emotion has the highest score
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
