#import time
radio.set_group(10)



def on_recieved_number(receivedNumber):
    if receivedNumber == 0:
        basic.show_arrow(ArrowNames.EAST)
        sphero.set_raw_motors(sphero.RawMotorModes.BACKWARD, 50, sphero.RawMotorModes.FORWARD, 50)
    if receivedNumber == 1:
        basic.show_arrow(ArrowNames.WEST)
        sphero.set_raw_motors(sphero.RawMotorModes.FORWARD, 50, sphero.RawMotorModes.BACKWARD, 50)
    if receivedNumber == 2:
        basic.show_arrow(ArrowNames.NORTH)
        sphero.set_raw_motors(sphero.RawMotorModes.FORWARD, 100, sphero.RawMotorModes.FORWARD, 100)
    if receivedNumber == 3:
        basic.show_arrow(ArrowNames.SOUTH)
        sphero.set_raw_motors(sphero.RawMotorModes.BACKWARD, 50, sphero.RawMotorModes.BACKWARD, 50)

radio.on_received_number(on_recieved_number)



def on_button_pressed_a():
    radio.send_number(0)

input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(1)

input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    radio.send_number(2)

input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_logo_pressed():
    radio.send_number(3)

    pass
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    if input.light_level()==0:
        sphero.set_rgb_led_by_index(sphero.LEDs.RIGHT_HEADLIGHT, 255, 255, 255)
        sphero.set_rgb_led_by_index(sphero.LEDs.LEFT_HEADLIGHT, 255, 255, 255)
        sphero.set_rgb_led_by_index(sphero.LEDs.RIGHT_BRAKELIGHT, 255, 0, 0)
        sphero.set_rgb_led_by_index(sphero.LEDs.LEFT_BRAKELIGHT, 255, 0, 0)
    else:
        sphero.set_all_leds(0,0,0)                        
basic.forever(on_forever)
