"""This module implements a Flask server for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handles requests to the /emotionDetector route.

    Retrieves the text to analyze from the request, calls the
    emotion_detector function, and returns the result.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Check for errors or None values in the response
    if 'error' in response or response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    response_text = (
        f"For the given statement, the system response is 'anger': {anger},"
        f" 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and"
        f" 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

    return response_text


@app.route("/")
def render_index_page():
    """Renders the index page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
