import requests
import sys
import re
if len(sys.argv) < 2:
    print("Usage: python3 version.py <url>")
    sys.exit(1)

base_url = sys.argv[1]

def check_version(url):
    target_url = f"{base_url}/administrator/manifests/files/joomla.xml"
    try:
        res = requests.get(target_url, timeout=10)
    #print(res.status_code)
        if res.status_code == 200:

            version = re.search(r'<version>(.*?)</version>', res.text)
            if version:
                print(f"[*] Joomla version found: {version.group(1)}")
            else:
                print("Nothing found about version")
        else:
            print(f"Unknown issue status code is {res.status_code}")
    except Exception as e:
        print(f"Error {e}")

if __name__ == "__main__":
    check_version(base_url)
