from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import base64
from pathlib import Path
from fastapi.responses import FileResponse


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RecognizerRequest(BaseModel):
    audioContent : str

@app.post("/recognize")
async def recognize(req: RecognizerRequest):
    print("Hello text")
    # Convert byte array
    bytes =base64.b64decode(req.audioContent)
    # Save in a file
    filename = "temp.wav"
    with open(filename, "wb") as f:
            f.write(bytes)

    return ("Hello Patient")


class SynthesizeResponse:
     audioContent:str

@app.get("/audio")
async def recognizer_audio():     
    with open("/home/eatl/patient-trigger/temp.wav", "rb") as audio_file:
        encoded_string = base64.b64encode(audio_file.read())

    response = SynthesizeResponse()
    response.audioContent = encoded_string

    return response
     