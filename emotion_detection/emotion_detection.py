import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL and headers (same as Task 2)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send the POST request
    response = requests.post(url, json=myobj, headers=headers)
    
    # Task 3: Convert the response text into a dictionary
    formatted_response = json.loads(response.text)
    
    # Extract the emotion dictionary from the nested response
    # The structure is: emotionPredictions -> [0] -> emotion
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Extract individual scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Write logic to find the dominant emotion
    # max() on the emotions dictionary finds the key with the highest value
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Create the final output dictionary format
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return result