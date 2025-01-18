# get_transcript/app.py
from flask import Flask, jsonify, request
from dapr.clients import DaprClient
import json

app = Flask(__name__)

@app.route('/get_transcript', methods=['GET'])
def get_transcript():
    data = request.json
    playlist_id = data.get('playlist_id')
    
    print(f"Received playlist_id: {playlist_id}")  # Debug log
    
    with DaprClient() as client:
        # Send JSON data properly encoded
        clean_data = json.dumps({
            "playlist_id": playlist_id,
            "raw_transcript": "example text"
        }).encode('utf-8')
        
        cleaned_response = client.invoke_method(
            app_id='clean-transcript',
            method_name='clean_transcript',
            data=clean_data,
            http_verb='get'
        )
        
        # Decode the response data from bytes
        cleaned_data = json.loads(cleaned_response.data.decode('utf-8'))
        
        return jsonify({
            "message": "Transcript service response",
            "playlist_id": playlist_id,
            "cleaned_response": cleaned_data
        })

if __name__ == '__main__':
    app.run(port=5001)