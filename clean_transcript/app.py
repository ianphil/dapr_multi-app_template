# clean_transcript/app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/clean_transcript', methods=['GET'])
def clean_transcript():
    data = request.json
    playlist_id = data.get('playlist_id')
    raw_transcript = data.get('raw_transcript')
    
    return jsonify({
        "message": "Clean transcript service response",
        "playlist_id": playlist_id,
        "cleaned_text": f"Cleaned version of: {raw_transcript}"
    })

if __name__ == '__main__':
    app.run(port=5002)