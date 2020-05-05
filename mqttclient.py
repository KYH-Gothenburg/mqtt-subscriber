import paho.mqtt.client as paho
from playsound import playsound

import webbrowser

def on_connect(client, userdata, flags, rc):
    print("Connected to server")
    # playsound('connected.wav')
    #print(client)
    #print(userdata)
    #print(flags)
    #print(rc)


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed")
    #playsound("subscribe.mp3")
    print(mid)
    print(granted_qos)

def on_message(client, userdata, msg):
    print(msg.topic)
    payload = msg.payload.decode('utf-8')

    print(payload)
    if payload == "1" or payload == "2" or payload == "3":
        playsound(payload +  ".wav")

    if msg.topic == "mqtt11/browse":
        webbrowser.open(payload)


def main():
    client = paho.Client()
    client.on_connect = on_connect
    client.connect('broker.hivemq.com', 1883)
    client.on_subscribe = on_subscribe
    client.subscribe("mqtt11/#", qos=1)
    #client.on_message = on_message
    client.loop_forever()


if __name__ == '__main__':
    main()