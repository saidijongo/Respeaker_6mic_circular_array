import time
import sys
sys.path.append('/home/pi/pixel_ring')
from pixel_ring import pixel_ring
import usb.core  # Import usb.core for Python 2

from gpiozero import LED

power = LED(5)
power.on()

pixel_ring.set_brightness(100)

def all_together_blink(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        pixel_ring.wakeup()
        time.sleep(0.5)
        pixel_ring.off()
        time.sleep(0.5)

def clockwise_blink(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(12):
            pixel_ring.set_color(i, 0, 255, 0)
            time.sleep(0.5)
            pixel_ring.set_color(i, 0, 0, 0)

def rainbow_effect(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(12):
            pixel_ring.set_color(i, 255, 0, 0)
        time.sleep(0.5)
        for i in range(12):
            pixel_ring.set_color(i, 0, 255, 0)
        time.sleep(0.5)
        for i in range(12):
            pixel_ring.set_color(i, 0, 0, 255)
        time.sleep(0.5)

if __name__ == '__main__':
    try:
        # Rotate LEDs in a ring for 60 seconds
        for _ in range(120):
            for i in range(12):
                pixel_ring.set_color(i, 0, 255, 0)
                time.sleep(0.5)
                pixel_ring.set_color(i, 0, 0, 0)

        # Blink all LEDs together for 30 seconds
        all_together_blink(30)

        # Blink LEDs one after another for 30 seconds
        clockwise_blink(30)

        # Display a rainbow effect for 30 seconds
        rainbow_effect(30)

    except KeyboardInterrupt:
        pass

    pixel_ring.off()
    time.sleep(1)

power.off()
