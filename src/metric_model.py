from pydantic import BaseModel

class Metric(BaseModel):
    metric_name: str
    payload: dict
    timestamp: int