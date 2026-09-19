from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import redis
import os

MODEL_PATH = "data/spam_model.joblib"

app = FastAPI(title="Spam Detection API")

model = joblib.load(MODEL_PATH)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    decode_responses=True
)

CACHE_TTL = 300


class MessageRequest(BaseModel):
    text: str


@app.get("/healthz")
def healthz():
    return {"status": "ok","version":"v2"}


@app.post("/predict")
def predict(request: MessageRequest):
    text = request.text

    # Check Redis cache
    cached_label = redis_client.get(text)

    if cached_label is not None:
        print("Cache hit")
        return {"label": cached_label}

    # Cache miss: run the model
    print("Cache miss")
    prediction = model.predict([text])[0]

    # Store prediction in Redis
    redis_client.setex(text, CACHE_TTL, prediction)

    return {"label": prediction}
