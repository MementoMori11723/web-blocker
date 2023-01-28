import datetime as dt
import time
from sys import platform
import socket

# please check if there is a host file or not

if platform == "linux" or platform == "linux2":
    path = '/etc/hosts'
    port = socket.gethostname()
elif platform == "darwin":
    path = '/etc/hosts'
    port = socket.gethostname()
elif platform == "win32":
    path = 'C:/Windows/System32/drivers/etc'
    port = socket.gethostname()

# Give a date like (2003 : year, 12 : month, 15 : date)
endDate = dt.datetime(2023, 1, 28)
siteBlock = ["www.facebook.com",
             "www.instagram.com"]  # you can add you websites

hostPath = path
redirect = port

while True:
    if dt.datetime.now() < endDate:
        print("Starting blocking")
        with open(hostPath, "r+") as hostFile:
            contant = hostFile.read()
            for website in siteBlock:
                if website not in contant:
                    hostFile.write(redirect+" "+website+"\n")
                else:
                    pass
    else:
        with open(hostPath, "r+") as hostFile:
            contant = hostFile.readlines()
            hostFile.seek(0)
            for lines in contant:
                if not any(website in lines for website in siteBlock):
                    hostFile.write(lines)

            hostFile.truncate()

        time.sleep(5)
