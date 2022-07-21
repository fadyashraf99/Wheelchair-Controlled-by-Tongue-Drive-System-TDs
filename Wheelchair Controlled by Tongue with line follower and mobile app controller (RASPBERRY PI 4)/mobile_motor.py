import motor as mot

#client.loop_forever()
import paho.mqtt.client as mqtt #import the client1
import time
import asyncio
msg = ""
############
def on_message(client, userdata, message):
    print("message received : " ,str(message.payload.decode("utf-8")))
    dir = str(message.payload.decode("utf-8"))
    if dir == ('UP'):
        mot.forward()
    elif dir == ('DOWN'):
        mot.backward()
    elif dir == ('RIGHT'):
        mot.right()
    elif dir == ('LEFT'):
        mot.left()
    elif dir == ('HONK'):
        mot.honky()
    else:  # stop
        mot.stop()
    print("message topic=",message.topic)
    if message.payload == "":
        msg = "3ala allah"
    else :
        msg = message.payload

    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)
def on_log(client, userdata, level, buf):
    print("log: ",buf)
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected success")
        print(f"Connected with result code {rc}")
        client.subscribe("test/fady2")
    else:
        print(f"Connected fail with code {rc}")
########################################
broker_address="broker.mqttdashboard.com" 
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_log=on_log # set client logging
client.on_connect = on_connect 
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.publish("test/fady1","lalalalalalalaala")
#client.publish("test/fady2","la")
#client.loop_start() #start the loop
print("Subscribing to topic","test/fady2")
client.subscribe("test/fady2")
#time.sleep(4) # wait
client.loop_forever(timeout = 20.0)


#client.subscribe("test/fady1")
#print("Publishing message to topic","house/bulbs/bulb1")
#client.publish("test/fady1","lalalalalalalaala")
#time.sleep(400000) # wait
#client.loop_forever()
#client.loop_stop() #stop the loop

