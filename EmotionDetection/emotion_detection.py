import json
import requests

def emotion_detector(text_to_analyse):
    """
    Takes in a text and, using Watson NLP library, 
    it returns the corresponding emotions and confidence scores  
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime' \
    '.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    formatted_response = json.loads(response.text)
    all_emotions = {}
    dominant_emotion_score = 0
    dominant_emotion = ""

    for item in formatted_response['emotionPredictions']:
        for emotion, score in item['emotion'].items():
            all_emotions[emotion] = score
            if score > dominant_emotion_score:
                dominant_emotion_score = score
                dominant_emotion = emotion
    all_emotions.update({'dominant_emotion':dominant_emotion})
    print(json.dumps(all_emotions, indent=4))

    return all_emotions

if __name__ == "__main__":
    emotion_detector("I love this new technology")
    