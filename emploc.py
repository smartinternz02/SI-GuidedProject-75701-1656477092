#IBM Watson IOT Platform
#pip install wiotp-sdk
import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "92xo80",
        "typeId": "node",
        "deviceId":"12357"
    },
    "auth": {
        "token": "employeeid12345"
    }
}
def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    emp_dic = {'AngelBonnie':1780,'Frank':1781,'Joe':1782,'Kimberly':1783,'Lisa':1784,'Michael':1785,'Patrick':1786,'Rose':1787,'Todd':1788,'Roja':1789}
    print(emp_dic )
    empid=random.randint(1780,1789)
    longitude = "78.5456505"
    latitude = "17.4226372"
    myData={'employeeid':empid,'longitude':longitude,'latitude':latitude}
    enteremployeeid = int(input("Enter employee id : "))
    if enteremployeeid in emp_dic.values():
        print("IT IS VALID EMPLOYEE ID ")
    elif enteremployeeid not in emp_dic.values():
        print("INVALID EMPLOYEE ID ")
        print("TRY AGAIN ")
    result=[new_k for new_k in  emp_dic.items() if new_k[1] == enteremployeeid][0][0]    
    print("YOU CAN ENTER INTO THE ROOM WELCOME  "  +result)
    client.publishEvent(eventId="status", msgFormat="json", data=myData , qos=0, onPublish=None)
    client.commandCallback = myCommandCallback
    time.sleep(1)
client.disconnect()
