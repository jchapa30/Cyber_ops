import requests
import json
import random
import time

# URL for Splunk's HTTP Event Collector (HEC)
SPLUNK_HEC_URL = "http://127.0.0.1:8000/services/collector/event"
SPLUNK_TOKEN = "abcde1e6-5e2c-4876-826e-b12f4c326231"  

# Function to generate a random log
def generate_log():
    return {
        "event": "cyber_event",
        "source": "firewall",
        "severity": random.choice(["low", "medium", "high"]),
        "message": "Detected suspicious activity",
        "timestamp": int(time.time())
    }

# Function to send the generated log to Splunk using HEC
def send_log_to_splunk(log):
    headers = {"Authorization": f"Splunk {SPLUNK_TOKEN}"}
    response = requests.post(SPLUNK_HEC_URL, headers=headers, data=json.dumps(log))
    
    # Checking for a successful response from Splunk
    if response.status_code != 200:
        print(f"Error sending log: {response.status_code} {response.text}")
    else:
        print(f"Successfully sent log: {log}")

# Main loop to continuously send logs every 5 seconds
if __name__ == "__main__":
    while True:
        log = generate_log()
        send_log_to_splunk(log)
        time.sleep(5)
