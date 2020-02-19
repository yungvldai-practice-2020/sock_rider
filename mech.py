import RPi.GPIO as GPIO


pins_on = [21, 22, 23, 24]


def left_right_motors_off():
    for pin in pins_on:
        GPIO.output(pin, False)


def left_motor_on(ward):
    level = True if ward == 'forward' else False
    GPIO.output(21, level)
    GPIO.output(22, not level)


def right_motor_on(ward):
    level = True if ward == 'forward' else False
    GPIO.output(23, level)
    GPIO.output(24, not level)


def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for pin in pins_on:
        GPIO.setup(pin, GPIO.OUT)
    left_right_motors_off()


def go(direction):
    print('go', direction)
    right_motor_on(direction)
    left_motor_on(direction)


def stop():
    print('stop')
    left_right_motors_off()


def turn(direction):
    print('turn', direction)
    if direction == 'left':
        left_motor_on('forward')
        right_motor_on('backward')
    else:
        left_motor_on('backward')
        right_motor_on('forward')
