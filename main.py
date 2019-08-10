# Write your code here :-)
import socket
from machine import Pin
import time
import random

SLEEP_TIME_MS = 30000
STATE_ENDPOINT = '' # your endpoint to provide a 0 or 1 state

def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    data_stitch = ""
    while True:
        data = s.recv(100)
        if data:
            data_stitch += str(data, 'utf8')

        else:
            break
    data_pack = data_stitch.split('\r\n\r\n')
    payload = data_pack[1] if len(data_pack) > 1 else ""
    s.close()
    return payload

def light_show(state: int):
    red_led = Pin(0, Pin.OUT)
    green_led = Pin(2, Pin.OUT)
    blue_led = Pin(4, Pin.OUT)
    if not state:
        red_led.value(0)
        green_led.value(0)
        blue_led.value(0)

        return
    red_led.value(random.getrandbits(1))
    green_led.value(random.getrandbits(1))
    blue_led.value(random.getrandbits(1))




def main():
    print('We are golden!')
    while True:
        lamp_state = int(http_get(STATE_ENDPOINT))
        print('Lamp state:', str(lamp_state))
        light_show(lamp_state)
        time.sleep_ms(SLEEP_TIME_MS)

if __name__ == "__main__":
    main()
