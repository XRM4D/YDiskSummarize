from flask import Blueprint, jsonify, request

api_endpoint = Blueprint('api', __name__)

@api_endpoint.route('/summarize', methods=['POST'])
def summarize():
    return 'summarize'