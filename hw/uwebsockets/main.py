"""Main is in the game."""
import network
import sys
import uwebsockets.client
import uwebsockets.protocol
from machine import Pin

# Create station and access point interfaces.
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)

# Activate station interface and deactivate access point interface to create a device instead of a router.
sta_if.active(True)
ap_if.active(False)

# Connect station interface with WiFi, wait until they are connected.
sta_if.connect("Lapikud", "wifiparool")
while not sta_if.isconnected(): pass

# Create object to turn on and off the pinout.
pin_to_relay = Pin(2, Pin.OUT)

# Save the socket address to string.
uri = "ws://iot.wut.ee:80/ws/lap_esimene_lamp"

# Connect with websocket and greet the server.
print("I shall try to acquire a channel of communication:\n", uri)
light1_web_socket = uwebsockets.client.connect(uri)
light1_web_socket.send("I am foremost pleased to meet you.")

# Keep updating the lamp state forever.
while True:
    try:
        # Receive data from server websocket.
        data = light1_web_socket.recv()
    except OSError: # Connection timeout or reset
        sys.exit() # Soft reset

    # Update the pinout.
    # Turn light on.
    if data == "1":
        pin_to_relay.on()

    # Turn light off.
    elif data == "0":
        pin_to_relay.off()

    # Send state to websocket.
    elif data == "?":
        light1_web_socket.send(str(pin_to_relay.value()))

    # Do nothing.
    else:
        pass