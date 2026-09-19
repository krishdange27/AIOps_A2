FROM python:3.11-slim

WORKDIR /app

COPY validate_shard.py .
COPY signup_shards ./signup_shards

CMD ["python", "validate_shard.py"]
