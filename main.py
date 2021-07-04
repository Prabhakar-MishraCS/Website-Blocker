

import datetime
import time
from datetime import datetime as dt
from plyer import notification

# change hosts path according to your OS
hosts_path = "/etc/hosts"
# localhost's IP
redirect = "127.0.0.1"

# websites That you want to block
website_list =["https://www.linkedin.com/","www.linkedin.com/","https://www.linkedin.com/feed/"
 "www.gmail.com", "www.youtube.com","https://www.youtube.com/","youtube.com"]

print(datetime.datetime.now())

while True:

    # time of your work
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("\nWorking Hours...")

        notification.notify(
            title="Working Hours",
            message=" Time to stay productive and slay the beast)",
            #app_icon="/Users/prabhms/PycharmProjects/Flipkart/fk.png",
            # displaying time
            timeout=4
        )

        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                # mapping hostnames to your localhost IP address
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)

        # removing hostnmes from host file
            file.truncate()

        print("\nChill Hours... ^_^")
    time.sleep(180)