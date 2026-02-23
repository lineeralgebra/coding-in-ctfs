import hashlib

salt = "8Sb)tM1vs1SS"

with open("hashes.txt", "r") as f:
    hashes = set(line.strip() for line in f)

print(f"[+] Loaded {len(hashes)} hashes")

with open("/usr/share/wordlists/rockyou.txt", "r", errors="ignore") as wordlist:
    for word in wordlist:
        word = word.strip()

        hash1 = hashlib.sha256((word + salt).encode()).hexdigest()
        hash2 = hashlib.sha256((salt + word).encode()).hexdigest()

        if hash1 in hashes:
            print(f"[+] FOUND (pass+salt): {word} -> {hash1}")

        if hash2 in hashes:
            print(f"[+] FOUND (salt+pass): {word} -> {hash2}")