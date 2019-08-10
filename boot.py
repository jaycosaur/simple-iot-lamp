# Write your code here :-)

WIFI_SSID = "" # Wifi SSid here
WIFI_PASS = "" # Wifi password here

def do_connect():
    import network
    sta = network.WLAN(network.STA_IF)
    if not sta.isconnected():
        print("connecting to network ...")
        sta.active(True)
        sta.connect(WIFI_SSID, WIFI_PASS)
        while not sta.isconnected():
            pass
        print('network config:', sta.ifconfig())

do_connect()
