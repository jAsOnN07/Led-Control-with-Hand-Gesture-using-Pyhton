import pyfirmata2
# Go to device manager and change the comport for your Arduino board
comport = 'COM5'
# creating pyfirmata2 Arduino instance
board = pyfirmata2.Arduino(comport)

# Initializing Arduino pin and pinmode
led_1 = board.get_pin('d:11:p')  # pin : 11
led_2 = board.get_pin('d:10:p')  # pin : 10
led_3 = board.get_pin('d:9:p')  # pin : 9
led_4 = board.get_pin('d:6:p')  # pin : 6
led_5 = board.get_pin('d:5:p')  # pin : 5


def led(total, distance):  # function to control led

    value = distance * (1 / 500)  # to convert length between index and thumb fingers to 0-1
    if total == 0:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)  # to turn on 0 leds
        led_4.write(0)
        led_5.write(0)
    elif total == 1:
        led_1.write(value)
        led_2.write(0)
        led_3.write(0)  # to turn on 1 leds
        led_4.write(0)
        led_5.write(0)
    elif total == 2:
        led_1.write(value)
        led_2.write(value)
        led_3.write(0)  # to turn on 2 leds
        led_4.write(0)
        led_5.write(0)
    elif total == 3:
        led_1.write(value)
        led_2.write(value)
        led_3.write(value)  # to turn on 3 leds
        led_4.write(0)
        led_5.write(0)
    elif total == 4:
        led_1.write(value)
        led_2.write(value)
        led_3.write(value)  # to turn on 4 leds
        led_4.write(value)
        led_5.write(0)
    elif total == 5:
        led_1.write(value)
        led_2.write(value)
        led_3.write(value)  # to turn on 5 leds
        led_4.write(value)
        led_5.write(value)
