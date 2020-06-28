import paho.mqtt.client as mqtt
import time,logging

broker="test.mosquitto.org"
port=1883

CLEAN_SESSION=True
logging.basicConfig(level=logging.INFO) 

def on_subscribe(client, userdata, mid, granted_qos):   
   time.sleep(1)
   logging.info("sub acknowledge message id="+str(mid))
   pass

def on_disconnect(client, userdata,rc=0):
    logging.info("DisConnected result code "+str(rc))


def on_connect(client, userdata, flags, rc):
    logging.info("Connected flags"+str(flags)+"result code "+str(rc))


def on_message(client, userdata, message):
    msg=str(message.payload.decode("utf-8"))
    print("message received  "  +msg)
    
def on_publish(client, userdata, mid):
    logging.info("message published "  +str(mid))

topic1 ="house/client_b"
client= mqtt.Client("ClientB",False)       

client.on_subscribe = on_subscribe   
client.on_disconnect = on_disconnect 
client.on_connect = on_connect 
client.on_message=on_message
client.connect(broker,port)           #establish connection
time.sleep(1)
client.loop_start()
client.subscribe("house/client_a")
count=1
while True: 
   print("publishing on topic ",topic1)
   msg="message " +str(count) + " from client B"
   #client.publish(topic1,msg)
   count +=1
   time.sleep(5)
client1.disconnect()

client1.loop_stop()

