from fastapi import FastAPI
import json
from database import redis_client
from metric_model import Metric


app = FastAPI()

@app.post("/metrics")
async def add_metric(metric: Metric):
    payload = metric.payload
    name = metric.metric_name
    timestamp = metric.timestamp

    json_payload = json.dumps(payload)

    value = {
        "payload": json_payload,
        "timestamp": timestamp
    }

    redis_client.rpush(name, value)

    return { "status": "ok" }


