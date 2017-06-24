
import paho.mqtt.client as paho
 
def on_connect(client, userdata, flags, rc):
    print('CONNACK received with code %d.' % (rc))
 
client = paho.Client()
client.on_connect = on_connect
client.connect('localhost', 1883)
client.publish('teste','outTopic',1)
