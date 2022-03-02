#!/usr/bin/env python3

import requests

response = requests.get("http://localhost:8000/health")

if response.status_code == 200:
  exit(0)
else:
  exit(1)
