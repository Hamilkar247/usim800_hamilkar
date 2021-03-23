from usim800_hamilkar.usim800_hamilkar import sim800
import os
import json

def testPrint(r):
    print("statusCode:"+str(r.status_code))
    print("content:"+str(r.content))
    print("json:"+str(r.json()))
    print("IP:"+str(r.IP))

def downloadConfig():
    gsm.requests.get(url="http://134.122.69.201/configKozienice/")
    r = gsm.requests
    testPrint(r)
    if os.path.isfile('config.json'):
      print("juz byl config")
    else:
        f=open("config.json", "w+")
    with open("config.json", 'wb') as file_json:
        file_json.write(r.content)

def downloadPicture():
    gsm.requests.get(url="https://134.122.69.201/widgetKozienice/")
    r = gsm.requests
    testPrint(r)
    if os.path.isfile('widget.png'):
       print("już był widget.png")
    else:
        f=open("widget.png", "w+")
    with open("widget.png", "wb") as widgetpng:
        widgetpng.write(r.content)

def send_sms():
    gsm.sms.send("+48532819627", "Royal canadian mounted police")

if __name__ == "__main__":
    gsm  = sim800(baudrate=9600, path="/dev/ttyAMA0")
    gsm.requests._APN = "internet"
    downloadConfig()
    downloadPicture()
    #send_sms()

