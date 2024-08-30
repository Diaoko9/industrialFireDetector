from opcua import Client, ua
import opcua.common

import numpy as np
import cv2
import time


def readNode(nodeAndIndex):
    out = client.get_node(nodeAndIndex)
    Output = out.get_value()
    return 0 if  Output==False else 1

def writeNode(nodeAndIndex, value):
    out = client.get_node(nodeAndIndex)
    Output = out.set_value(ua.DataValue(ua.Variant(value, ua.VariantType.Boolean)))



url = 'opc.tcp://192.168.0.1:4840'

client = Client(url)

client.session_timeout = 10000
client.connect()

client.get_namespace_index('http://Server interface_1')

out1 = client.get_node('ns=4;i=2')
out2 = client.get_node('ns=4;i=3')
opcInput = readNode(out1)
Output = readNode(out2)

fire_cascade = cv2.CascadeClassifier('Haarcascades/cascade_fire.xml')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret. img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(gray, 2, 5)

    for (x, y, w, h) in fire :
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        time.sleep(0.2)

        if fire != n:
            opcInput = writeNode('ns=4, i=2', True)
        elif fire == () :
            opcInput = writeNode('ns=4, i=2', False)

    cv2.imshow('img', img)
    k = cv2.waitkey(1)
    if k == 99 :
        break
cv2.destroyAllWindows()
