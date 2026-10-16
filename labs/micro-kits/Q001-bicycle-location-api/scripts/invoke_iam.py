#!/usr/bin/env python3
"""Call IAM-protected Q001 HTTP API once; synthetic data only, no access keys logged."""
import argparse
import json
import sys
from urllib import error, request as urlrequest

import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--url", required=True)
    p.add_argument("--region", required=True)
    p.add_argument("--profile")
    p.add_argument("--invalid", action="store_true")
    args = p.parse_args()
    if not args.url.startswith("https://") or not args.url.endswith("/locations"):
        p.error("URL must use HTTPS and end in /locations")
    session = boto3.Session(profile_name=args.profile) if args.profile else boto3.Session()
    creds = session.get_credentials()
    if creds is None:
        raise SystemExit("No credentials; configure SSO or AWS profile first")
    payload = {"bike_id": "BIKE-101", "latitude": 95 if args.invalid else 53.5511, "longitude": 9.9937}
    signed = AWSRequest(method="POST", url=args.url, data=json.dumps(payload).encode("utf-8"),
                        headers={"Content-Type": "application/json"})
    SigV4Auth(creds.get_frozen_credentials(), "execute-api", args.region).add_auth(signed)
    prepared = signed.prepare()
    req = urlrequest.Request(args.url, data=prepared.body, headers=dict(prepared.headers), method="POST")
    try:
        with urlrequest.urlopen(req, timeout=12) as response:
            print("HTTP", response.status, response.read().decode())
    except error.HTTPError as exc:
        print("HTTP", exc.code, exc.read().decode())
        if not (args.invalid and exc.code == 422):
            sys.exit(1)

if __name__ == "__main__":
    main()
