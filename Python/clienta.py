import paho.mqtt.client as mqtt
import time,logging
import sys

start_time1 =time.time()
broker="test.mosquitto.org"

port=1883
messagesent=1000

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

topic1 ="house/client_a"
client= mqtt.Client("ClientA",False)       #create client 
#msg="Avantages Azure IoT Les clients existants soulignent divers avantages de Microsoft Azure en fonction des spécificités de leur secteur Simplicité. Microsoft a vraiment investi pour rendre sa plateforme IoT pratique et simple pour différents utilisateurs, quelles que soient leurs compétences. De la connexion dTarification flexible. Chaque service Azure IoT a son propre modèle de tarification, en fonction de ses spécificités et de ses fonctionnalités. Ce qui distingue vraiment la tarification Azure IoT, capproche simple et la transparence. Par exemple, le coût du combo Amazon Sphere (puce, système dutilisation populaires dans Azure IoT Central. Ou se compose entièrement dAccuweather. Le service Azure Digital Twins  permet de créer une représentation virtuelle de l’environnement IoT physique et de déterminer les dépendances, corrélations et relations entre ses parties. Une sécurité renforcée. LAzure IoT estRéseau de partenaires puissant. Tout comme AWS, Azure a une l"
msg="Avantages Azure"
def utf8len(s):
    return len(s.encode('utf-8'))

client.on_subscribe = on_subscribe   
client.on_disconnect = on_disconnect 
client.on_connect = on_connect 
client.on_message=on_message
client.connect(broker,port)           
time.sleep(1)
client.loop_start()
client.subscribe("house/client_b")
count=1
count1=0
msg+=msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg
msg+=msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg+msg



print(" The nomber of messages is : " + str(messagesent))
#print(" The size of the message is sys : " + str(sys.getsizeof(msg)) + " bytes")
print(" The size of the message is utf8 : " + str(utf8len(msg)) + " bytes")
#print(" The size of the message is len : " + str(len(msg)) + " bytes")

temp =0
#while True: #runs forever 
while ( count1 <1) :
   print("publishing on topic ",topic1)

  
   start_time =time.time()
   for i in range (messagesent) :

     
     print ("Message number : " +str(count) +" from client A" )
     
     start_time2 =time.time()
     client.publish(topic1,msg)
     end_time2= time.time()
     duration3 =end_time2 - start_time2
     temp= temp+ duration3
     #print("the time to send this message is :"+str(duration3) + " Seconds ")
     #print("all times is :"+str(temp) + " Seconds ")      
     count +=1
   end_time= time.time()
   duration =end_time - start_time
   print("the average time to send a single message is :"+str(temp/messagesent) + " Seconds ")  
   print("the net time to send " + str(messagesent) +" messages is : " +str(temp) + " Seconds ")    
   print("time left in the loop to send " + str(messagesent) +" messages is : " +str(duration) + " Seconds ")    
   start_time=0
   temp=0
   end_time=0
   time.sleep(5)
   count1= count1 +1
client.disconnect()

client.loop_stop()
end_time1= time.time()
duration1 =end_time1 - start_time1
print("Program execution time is : "+str(duration1) + " Seconds ")   

