"""
Deploys Flash web server
"""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def detect():
    """Will collect the text_to_analyse query from the get method 
    and return a sentiment analysis for the text"""

    text_to_analyse = request.args.get('text_to_analyse')

    status_code = 200
    if not text_to_analyse:
        status_code = 400

    response_dict = emotion_detector(text_to_analyse, status_code = status_code)


    formatted_response = f"""For the given statement, the system response is
     'anger': {response_dict['anger']},
     'disgust': {response_dict['disgust']}, 
     'fear': {response_dict['fear']}, 
     'joy': {response_dict['joy']} and
     'sadness': {response_dict['sadness']}.
     The dominant emotion is {response_dict['dominant_emotion']}."""

    if response_dict['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return formatted_response
