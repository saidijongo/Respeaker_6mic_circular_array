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

if __name__ == '__main__':
    try:
        # Blink all LEDs together for 10 seconds
        all_together_blink(10)

        # Blink LEDs one after another in a clockwise direction for 10 seconds
        clockwise_blink(10)
    except KeyboardInterrupt:
        pass

    pixel_ring.off()
    time.sleep(1)

power.off()

