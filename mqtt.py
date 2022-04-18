import paho.mqtt.client as mqtt
import time

# Example code to test MQTT in Python3

# Steps:
# create client instance
# connect to broker
# subscribe to topic
# publish message

def on_message(client, userdata, message):
    if message:
        print("Message Received: ", message.payload.decode("utf-8"))
        print("Topic: ", message.topic)
        print("Qos: ", message.qos)
        print("Flag: ", message.retain)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Disconnected")

def connect():
    broker = "mqtt.eclipseprojects.io"
    client_name = "testing"

    client = mqtt.Client(client_name)
    client.on_message = on_message
    client.connect(broker)

    client.loop_start()

    topic = "Test Topic"
    publish = "Example message"

    print("Started Loop")
    print("----------")
    print("Subscribing to", topic)
    client.subscribe(topic, qos=0)

    print("Publishing message...")
    client.publish("Test Topic", publish)
    print()

    time.sleep(1)
    
    client.on_disconnect = on_disconnect
    client.loop_stop()
    print("Loop stopped.\n")

    sock = client.socket()
    print(sock)
if __name__ == "__main__":
    connect()
