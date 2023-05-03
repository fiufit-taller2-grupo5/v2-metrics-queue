from fastapi import FastAPI
import json
from database import redis_client
from metric_model import Metric


app = FastAPI()

@app.post("/metrics")
async def add_metric(metric: Metric):
    timestamp = metric.timestamp
    value = { "payload": json.dumps(metric.payload), "timestamp": timestamp }

    redis_client.rpush(metric.metric_name, json.dumps(value))

    return { "status": "ok" }

