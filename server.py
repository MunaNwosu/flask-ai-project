''' Executing this function initiates the application of emotion detection
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_emotion():
    ''' This code receives the text from the HTML interface and 
        runs emotional detecttion over it using emotion_detector()
        function. The output returned shows the emotions and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Invalid input. Enter a valid text"
    output = emotion_detector(text_to_analyze)
    emotion = []
    score = []
    for key,value in output.items():
        emotion.append(key)
        score.append(value)

    if output['dominant_emotion'] is None:
        return "Invalid input. Enter a valid text"


    return f"For the given statment, the system response is {emotion[0]} : {score[0]}, " \
    f"{emotion[1]} : {score[1]}, {emotion[2]} : {score[2]}, {emotion[3]} : {score[3]} " \
    f"{emotion[4]} : {score[4]}. The dominant emotion is {score[5]}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
