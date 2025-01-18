# get_playlist/app.py
from flask import Flask, jsonify
from dapr.clients import DaprClient
import json

app = Flask(__name__)

@app.route('/get_playlist', methods=['GET'])
def get_playlist():
    with DaprClient() as client:
        # Send JSON data properly encoded
        data = json.dumps({"playlist_id": "123"}).encode('utf-8')
        
        transcript_response = client.invoke_method(
            app_id='get-transcript',
            method_name='get_transcript',
            data=data,
            http_verb='get'
        )
        
        # Decode the response data from bytes
        transcript_data = json.loads(transcript_response.data.decode('utf-8'))
        
        return jsonify({
            "message": "Playlist service response",
            "transcript_response": transcript_data
        })

if __name__ == '__main__':
    app.run(port=5000)