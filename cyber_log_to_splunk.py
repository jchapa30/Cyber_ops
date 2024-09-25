import json
import time
import random
import requests

# URL for Splunk's HTTP Event Collector (HEC)
SPLUNK_HEC_URL = "http://127.0.0.1:8000/services/collector/event"
SPLUNK_TOKEN = "abcde1e6-5e2c-4876-826e-b12f4c326231"  

headers = {"Authorization": f"Splunk {SPLUNK_TOKEN}"}

def generate_log():
    log_data = {
        "event": {
            "timestamp": time.time(),
            "threat": random.choice(["DDoS", "Phishing", "Malware"]),
            "severity": random.choice(["low", "medium", "high"]),
            "source_ip": ".".join(str(random.randint(0, 255)) for _ in range(4)),
            "destination_ip": ".".join(str(random.randint(0, 255)) for _ in range(4)),
            "protocol": random.choice(["TCP", "UDP", "HTTP", "HTTPS"]),
        },
        "sourcetype": "_json",
        "index": "cybersecurity_logs"
    }
    return json.dumps(log_data)

while True:
    log = generate_log()
    response = requests.post(SPLUNK_HEC_URL, headers=headers, data=log)
    print(f"Sent log with status code {response.status_code}")
    time.sleep(2)
