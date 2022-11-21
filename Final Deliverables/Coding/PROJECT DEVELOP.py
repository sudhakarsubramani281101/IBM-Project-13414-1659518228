LOCATION:

import wiop.sdk.device
import time
import random
myConfig={
      "Identity":{
         "orgId": "gagtey",
         "typeId": "GPS",
         "deviceId": "12345"
       }
       "auth": {
         "token": "12345678"
       }
}
def myCommandCallback(cmd):
       print("Message received from IBM IoT Platform: %s" %cmd.data['command']
       m=cmd.data['command']
client=wiotp.sdk.device.DeviceClient(config=myConfig,logHandlers=None)
client.connect()
def pub(data):
       client.publishEvent(eventId="status",msgFormat="json",data=myData,qos=0,
       print("Published data Successfully: %s",myData)
while true:
       myData={'name':'Train1','lat',:17.6387448,'lon':78.4754336}
       pub(myData)
       time.sleep(3)
       myData={'name':'Train1','lat',:17.6341908,'lon':78.4744722}	
       pub(myData)
       time.sleep(3)
       myData={'name':'Train1','lat',:17.6340889,'lon':78.4745052}
       pub(myData)
       time.sleep(3)
       myData={'name':'Train1','lat',:17.6248626,'lon':78.4720259}
       pub(myData)
       time.sleep(3)
       myData={'name':'Train1','lat',:17.6188577,'lon':78.4698726}
       pub(myData)
       time.sleep(3)
       myData={'name':'Train1','lat',:17.6132382,'lon':78.4707318}
       pub(myData)
       time.sleep(3)
       client.commandCallback=myCommandCallback
client.disconnect()

TIME SIGNAL:

import cv2
import numpy as np
import time
import pyzbar.pyzbar as pyzbar
from ibmcloudant.cloudant_v1 import CloudantV1
from ibmcloudant import CouchDbSessionAuthenticator
from ibm_cloud-sdk_core.authenticaters import BasicAuthenticator
authenticator=BasixAuthenticator('apikey-v2-16u3crmdpkghhxefdikvpssoh5fwezrmuup5fv5g3ubz','b0ab119f45d3e6255eabb978')
service=CloudantV1(authenticator=authenticator)
service.set_service_url('http://apikey-v2-16u3crmdpkghhxefdikvpssoh5fwezrmuup5fv5g3ubz','b0ab119f45d3e6255eabb978')
cap=cv2.VideoCapture(0)
font=cv2.FONT_HERSHEY_PLAIN
while True:
     _,frame=cap.read()
     decodedObjects=pyzbar.decode(frame)
     for obj in decodedObjects:
        #print("Data",obj.data)
        a=obj.data.decode('UTF-8')
        cv2.puText(frame,"Ticket",(50,50),font,2,(255,0,0),3)
        #print(a)
        try:
          response=service.get_document(
             db='booking',
             doc_id=a
             ).get_result()
           print(response)
           time.sleep(5)
       except Exception as e:
           print("Not a Valid Ticket")
           time.sleep(5)
    cv2.imshow("Frame",frame)
    if cv2.waitkey(1)&0xFF==ord('q'):
cap.release()
cv2.destroyAllWindows()
client.disconnect()

SPRINT 1 :

#include <LiquidCrystal.h>  
LiquidCrystal 1cd(5,6,8,9,10,11);   
int red1ed = 2; 
int green1ed = 3; 
int buzzer = 4; 
int sensor = A0;  
int sensorThresh = 400;  
  
  
void setup()  
{  
pinMode(red1ed, OUTPUT); 
pinMode(green1ed,OUTPUT); 
pinMode(buzzer,OUTPUT); 
pinMode(sensor,INPUT); 
serial.begin(9600);  
1cd.begin(16,2);  
}  
  
  
Void loop()  
{  
  
int analogValue = analogRead(sensor); 
Serial.print(analogvalue); 
if(analogValue>sensorThresh)  
{  
  
digitalWrite(red1ed,HIGH);  
digit1Weite(green1ed,LOW); 
tone(buzzer,1000,10000);  
1cd.clear();  
1cd.setCursor(0,1); 
1cd.print(“RAILWAYS”); 
delay(1000); 
1cd.clear();  
1cd.setCursor(0,1);  
1cd.print(“SMART SOLUTION”); 
delay(1000);  
}  
  
else  
{  
  
digitalWrite(greenlad,HIGH); 
digitalWrite(red1ed,LOW); 
noTone(buzzer);  
1cd.clear();  
1cd.setCursor(0,0); 
1cd.print(“SAFE”); 
delay(1000); 
1cd.clear();  
1cd.setCursor(0,1);  
1cd.print(“ALL CLEAR”);
delay(1000);  
}  
}  