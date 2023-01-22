import datetime as dt
import time

endDate = dt.datetime()  # Give a date like (2003 : year, 12 : month, 15 : date)
siteBlock = ["www.youtube.com", "www.facebook.com",
             "www.instagram.com"]  # you can add you websites
# your host file (it will be in c:\Windows\System32\drivers\etc folder)
hostPath = ""
redirect = ""  # use your localhost number

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
