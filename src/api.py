from flask import Blueprint, request, jsonify
from src import yandex, transcription, summarization
import os

api_endpoint = Blueprint('api', __name__)

@api_endpoint.route('/summarize', methods=['POST'])
def summarize():
    if 'link' not in request.json or  \
        'language' not in request.json \
        or 'min' not in request.json or \
        'max' not in request.json:
        return 'Missing parameters', 400

    yandex.download_video(request.json['link'], 'video.mp4')
    yandex.extract_audio('video.mp4', 'audio.wav')

    text = transcription.transcribe_audio('audio.wav', request.json['language'])
    summarized = summarization.summarize(text, request.json['min'], request.json['max'])

    os.remove("audio.wav")
    os.remove("video.mp4")
    return jsonify({'text': summarized})



