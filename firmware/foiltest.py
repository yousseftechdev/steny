from machine import Pin
import time

touch_pin = Pin(0, Pin.IN)
led = Pin(25, Pin.OUT)

def read_touch(pin):
    # Charge the pad
    pin.init(Pin.OUT)
    pin.value(1)
    time.sleep_us(10)

    # Switch to input and time discharge
    pin.init(Pin.IN)

    t = 0
    while pin.value() == 1 and t < 1000:
        t += 1

    return t


while True:
    val = read_touch(touch_pin)
    
    if val < 35:
        led.value(1)
    else:
        led.value(0)

    time.sleep(0.08)

