from machine import Pin
import time

touch_pin1 = Pin(0, Pin.IN)
touch_pin2 = Pin(1, Pin.IN)
touch_pin3 = Pin(2, Pin.IN)
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
    val1 = read_touch(touch_pin1)
    val2 = read_touch(touch_pin2)
    val3 = read_touch(touch_pin3)
    
    if val1 < 35:
        led.value(1)
    elif val2 < 35:
        led.value(1)
    elif val3 < 35:
        led.value(1)
    else:
        led.value(0)

    time.sleep(0.08)