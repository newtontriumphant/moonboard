# Hi! This is moonboard's favorite rhythm! a 2-against-3 polyrhythm! :D I'm so glad it worked, I hope you enjoy.

import board
import digitalio
import time

red_led = digitalio.DigitalInOut(board.GP24)
red_led.direction = digitalio.Direction.OUTPUT
blue_led = digitalio.DigitalInOut(board.GP23)
blue_led.direction = digitalio.Direction.OUTPUT
red_led.value = False
blue_led.value = False
# Polyrythm parameters
tempo = 1.0
red_period = tempo * 2
blue_period = tempo * 3
start_time = time.monotonic()

while True:
    try:
        current_time = time.monotonic()
        
        if (current_time - start_time) % red_period < 0.1:
            red_led.value = True
        else:
            red_led.value = False
        if (current_time - start_time) % blue_period < 0.1:
            blue_led.value = True
        else:
            blue_led.value = False     
        time.sleep(0.01)
    except Exception as e:
        red_led.value = False
        blue_led.value = False
        print("Error occurred:", e)
        break
