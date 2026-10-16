"""Synthetic bicycle GPS receiver; validates but never stores data."""
import json
import math
import re

BIKE_ID = re.compile(r"^[A-Za-z0-9-]{1,32}$")

def response(status, body):
    return {"statusCode": status, "headers": {"content-type": "application/json"},
            "body": json.dumps(body)}

def valid_number(x, low, high):
    return type(x) in (float, int) and math.isfinite(x) and low <= x <= high

def lambda_handler(event, context):
    if not isinstance(event, dict):
        return response(400, {"error": "invalid_event"})
    if event.get("requestContext", {}).get("http", {}).get("method") != "POST":
        return response(405, {"error": "method_not_allowed"})
    raw = event.get("body")
    try:
        payload = json.loads(raw) if isinstance(raw, str) else raw
    except (json.JSONDecodeError, TypeError):
        return response(400, {"error": "invalid_json"})
    if not isinstance(payload, dict):
        return response(400, {"error": "json_object_required"})
    bike_id = payload.get("bike_id")
    if (not isinstance(bike_id, str)
            or not BIKE_ID.fullmatch(bike_id)
            or not valid_number(payload.get("latitude"), -90, 90)
            or not valid_number(payload.get("longitude"), -180, 180)):
        return response(422, {"error": "invalid_location_fields"})
    return response(202, {"accepted": True, "stored": False, "bike_id": bike_id,
                          "note": "synthetic validation only; no database"})
