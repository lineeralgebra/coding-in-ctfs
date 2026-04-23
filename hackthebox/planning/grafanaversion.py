import requests
import sys

if len(sys.argv) < 2:
    print("Usage: python3 test.py <url>")
    sys.exit(1)

base_url = sys.argv[1]

def vuln_check(url):
    check_url = f"{url.rstrip('/')}/api/health"

    try:
        vuln_res = requests.get(check_url, timeout=10)
        vuln_res.raise_for_status()
        data = vuln_res.json()
        version = data.get("version")

        if not version:
            print("[-] Could not retrieve version information.")
        else:
            print(f"[*] Detected Version: {version}")
            if version == "11.0.0":
                print(f"[!] Vulnerable to CVE-2024-9264")
            else:
                print("[+] Not vulnerable (version mismatch)")

        return version

    except requests.exceptions.RequestException as e:
        print(f"[-] Error connecting to {url}: {e}")
        return None

if __name__ == "__main__":
    vuln_check(base_url)
