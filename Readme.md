# Dapr Multi-Service Application

This repository contains a Dapr-enabled Python application with three services that interact with each other:

1. **Get Playlist Service** (`get_playlist`)
2. **Get Transcript Service** (`get_transcript`)
3. **Clean Transcript Service** (`clean_transcript`)

These services demonstrate inter-service communication using Dapr.

---

## Services Overview

### 1. **Get Playlist Service**
- **Path**: `get_playlist/app.py`
- **Description**: Invokes the `get_transcript` service to retrieve a transcript associated with a playlist.
- **Endpoint**: `/get_playlist` (HTTP GET)
- **Port**: 5000
- **Responsibilities**:
  - Sends a `playlist_id` to the `get_transcript` service.
  - Returns the response received from the `get_transcript` service.

### 2. **Get Transcript Service**
- **Path**: `get_transcript/app.py`
- **Description**: Receives a `playlist_id` and invokes the `clean_transcript` service to clean the raw transcript.
- **Endpoint**: `/get_transcript` (HTTP GET)
- **Port**: 5001
- **Responsibilities**:
  - Extracts the `playlist_id` from the incoming request.
  - Sends the `playlist_id` and a mock `raw_transcript` to the `clean_transcript` service.
  - Returns the cleaned transcript.

### 3. **Clean Transcript Service**
- **Path**: `clean_transcript/app.py`
- **Description**: Cleans the raw transcript provided by the `get_transcript` service.
- **Endpoint**: `/clean_transcript` (HTTP GET)
- **Port**: 5002
- **Responsibilities**:
  - Accepts a `playlist_id` and `raw_transcript`.
  - Returns a cleaned version of the transcript.

---

## Prerequisites

- Python 3.8+
- Dapr CLI
- Docker (optional, for containerized deployment)
- Flask (installed via pip)
- `dapr` Python SDK (installed via pip)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Install Dependencies

Navigate to each service directory and install dependencies:
```bash
python -m venv .venv
pip install -r requirements.txt
```

### 3. Install Dapr CLI
Follow the [official Dapr CLI installation guide](https://docs.dapr.io/getting-started/install-dapr-cli/).

### 4. Initialize Dapr
```bash
dapr init
```

### 5. Run the Application

#### Using Dapr Multi-App YAML:
Run all services simultaneously using the provided `dapr.yaml`:
```bash
dapr run -f dapr.yaml
```

#### Running Services Individually:
Alternatively, you can start each service manually:

1. **Get Playlist Service**:
   ```bash
   cd get_playlist
   dapr run --app-id get-playlist --app-port 5000 --dapr-http-port 3500 -- python app.py
   ```

2. **Get Transcript Service**:
   ```bash
   cd get_transcript
   dapr run --app-id get-transcript --app-port 5001 --dapr-http-port 3501 -- python app.py
   ```

3. **Clean Transcript Service**:
   ```bash
   cd clean_transcript
   dapr run --app-id clean-transcript --app-port 5002 --dapr-http-port 3502 -- python app.py
   ```

---

## Testing the Application

### Using Dapr CLI:
You can test the services directly using the Dapr CLI:
```bash
dapr invoke --app-id get-playlist --method get_playlist --verb GET
```

### Endpoints:

1. **Get Playlist**:
   - **URL**: `http://localhost:5000/get_playlist`
   - **Method**: GET
   - **Response**:
     ```json
     {
       "message": "Playlist service response",
       "transcript_response": {
         "message": "Transcript service response",
         "playlist_id": "123",
         "cleaned_response": {
           "message": "Clean transcript service response",
           "playlist_id": "123",
           "cleaned_text": "Cleaned version of: example text"
         }
       }
     }
     ```

2. **Get Transcript**:
   - **URL**: `http://localhost:5001/get_transcript`
   - **Method**: GET
   - **Request Body**:
     ```json
     {
       "playlist_id": "123"
     }
     ```
   - **Response**:
     ```json
     {
       "message": "Transcript service response",
       "playlist_id": "123",
       "cleaned_response": {
         "message": "Clean transcript service response",
         "playlist_id": "123",
         "cleaned_text": "Cleaned version of: example text"
       }
     }
     ```

3. **Clean Transcript**:
   - **URL**: `http://localhost:5002/clean_transcript`
   - **Method**: GET
   - **Request Body**:
     ```json
     {
       "playlist_id": "123",
       "raw_transcript": "example text"
     }
     ```
   - **Response**:
     ```json
     {
       "message": "Clean transcript service response",
       "playlist_id": "123",
       "cleaned_text": "Cleaned version of: example text"
     }
     ```

---

## Troubleshooting

- Ensure all Dapr sidecars are running on their respective ports.
- Verify Python dependencies are installed correctly.
- Check the logs of individual services for debugging information.

---

## Resources

- [Dapr Documentation](https://docs.dapr.io/)
- [Flask Documentation](https://flask.palletsprojects.com/)

---

## License

This project is licensed under the [MIT License](LICENSE).

