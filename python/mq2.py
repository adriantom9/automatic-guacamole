import paho.mqtt.client as mqttClient
import time
 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")
 
def on_message(client, userdata, message):
    dt = message.payload
    print "Message received: "  + dt
 
Connected = False   #global variable for the state of the connection
 
broker_address= "167.205.27.98"  #Broker address
 
client = mqttClient.Client("Python")               #create new instance
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
 
client.connect(broker_address)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
client.subscribe("pyex")
 
try:
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:
    print "exiting"
    client.disconnect()
    client.loop_stop()
