#import time
radio.set_group(10)



def on_recieved_number(receivedNumber):
    if receivedNumber == 0:
        basic.show_icon(IconNames.HAPPY)
        sphero.set_raw_motors(sphero.RawMotorModes.FORWARD, 100, sphero.RawMotorModes.BACKWARD, 100)
    if receivedNumber == 1:
        basic.show_icon(IconNames.SAD)
        sphero.set_raw_motors(sphero.RawMotorModes.BACKWARD, 100, sphero.RawMotorModes.FORWARD, 100)
    if receivedNumber == 2:
        basic.show_icon(IconNames.ASLEEP)
        sphero.set_raw_motors(sphero.RawMotorModes.FORWARD, 100, sphero.RawMotorModes.FORWARD, 100)
    if receivedNumber == 3:
        basic.show_icon(IconNames.GIRAFFE)
        sphero.wake()

radio.on_received_number(on_recieved_number)



def on_button_pressed_a():
    radio.send_number(0)
#    sphero.set_raw_motors(sphero.RawMotorModes.FORWARD, 100, sphero.RawMotorModes.FORWARD, 100)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(1)
#    sphero.set_raw_motors(sphero.RawMotorModes.BACKWARD, 100, sphero.RawMotorModes.BACKWARD, 100)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    radio.send_number(2)
#    sphero.set_raw_motors(sphero.RawMotorModes.OFF, 0, sphero.RawMotorModes.OFF, 0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)



def on_gesture_shake():
    if input.on_gesture == 1000 
    radio.send_number(3)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

    


def on_forever():
    if input.light_level()==0:
        sphero.set_rgb_led_by_index(sphero.LEDs.RIGHT_HEADLIGHT, 255, 255, 255)
        sphero.set_rgb_led_by_index(sphero.LEDs.LEFT_HEADLIGHT, 255, 255, 255)
        sphero.set_rgb_led_by_index(sphero.LEDs.RIGHT_BRAKELIGHT, 255, 0, 0)
        sphero.set_rgb_led_by_index(sphero.LEDs.LEFT_BRAKELIGHT, 255, 0, 0)
    else:
        sphero.set_all_leds(0,0,0)                        
basic.forever(on_forever)


# while True:
#     #display.scroll(display.read_light_level())
#     #sleep(1000)
#     if display.read_light_level()==0:
#         RVRLed.set_rgb_led_by_index(LEDs.RIGHT_BRAKELIGHT, red=255, green=0, blue=0)
#         RVRLed.set_rgb_led_by_index(LEDs.LEFT_BRAKELIGHT, red=255, green=0, blue=0)
#         RVRLed.set_rgb_led_by_index(LEDs.RIGHT_HEADLIGHT, red=255, green=255, blue=255)
#         RVRLed.set_rgb_led_by_index(LEDs.LEFT_HEADLIGHT, red=255, green=255, blue=255)

#     else:
#         RVRLed.set_all_leds(0,0,0)
        