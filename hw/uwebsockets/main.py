"""Main is in the game."""
import network
import sys
import uwebsockets.protocol
from machine import Pin

def toggle_light(pin_object):
    """Toggle the light."""
    print("Toggle used.")
    if pin_object.value():
        light_control_pin.off()

    else:
        light_control_pin.on()


# Create Pin objects to turn on and off the pinout and read switch's state.
light_control_pin = Pin(2, Pin.OUT)
switch_input_pin = Pin(0, Pin.IN)

# Assign callback function to switch_input_pin.
switch_input_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=toggle_light)

# Create station and access point interfaces.
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)

# Activate station interface and deactivate access point interface to create a device instead of a router.
sta_if.active(True)
ap_if.active(False)

# Connect station interface with WiFi, wait until they are connected.
sta_if.connect("Lapikud", "wifiparool")
while not sta_if.isconnected(): pass

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
        light_control_pin.on()

    # Turn light off.
    elif data == "0":
        light_control_pin.off()

    # Send state to websocket.
    elif data == "?":
        light1_web_socket.send(str(light_control_pin.value()))

    # Do nothing.
    else:
        pass
