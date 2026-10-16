"""Offline tests: no AWS credentials or network calls."""
import importlib.util
import json
from pathlib import Path
import unittest

BASE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("q001_handler", BASE / "lambda/handler.py")
handler = importlib.util.module_from_spec(spec)
spec.loader.exec_module(handler)

def invoke(payload, method="POST", raw=False):
    event = {"version": "2.0", "requestContext": {"http": {"method": method}},
             "body": payload if raw else json.dumps(payload)}
    res = handler.lambda_handler(event, None)
    return res["statusCode"], json.loads(res["body"])

class HandlerTests(unittest.TestCase):
    def test_valid(self):
        code, payload = invoke({"bike_id": "BIKE-101", "latitude": 53.55, "longitude": 9.99})
        self.assertEqual(code, 202)
        self.assertTrue(payload["accepted"])
        self.assertFalse(payload["stored"])
    def test_invalid_json(self):
        self.assertEqual(invoke("{", raw=True)[0], 400)
    def test_list_body(self):
        self.assertEqual(invoke([])[0], 400)
    def test_bad_latitude(self):
        self.assertEqual(invoke({"bike_id": "B-1", "latitude": 91, "longitude": 9})[0], 422)
    def test_bad_longitude(self):
        self.assertEqual(invoke({"bike_id": "B-1", "latitude": 1, "longitude": -181})[0], 422)
    def test_boolean_coords(self):
        self.assertEqual(invoke({"bike_id": "B-1", "latitude": True, "longitude": 10})[0], 422)
    def test_missing_bike_id(self):
        self.assertEqual(invoke({"latitude": 1, "longitude": 2})[0], 422)
    def test_wrong_method(self):
        self.assertEqual(invoke({"bike_id": "B-1", "latitude": 1, "longitude": 2}, "GET")[0], 405)
    def test_invalid_event(self):
        self.assertEqual(handler.lambda_handler(None, None)["statusCode"], 400)
    def test_no_persistence(self):
        src = (BASE / "lambda/handler.py").read_text()
        self.assertNotIn("boto3", src)
        self.assertNotIn("put_item", src)

if __name__ == "__main__":
    unittest.main()
