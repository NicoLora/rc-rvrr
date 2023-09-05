radio.set_group(10)

def on_recieved_number(receivedNumber):
    if receivedNumber == 0:
        sphero.set_raw_motors(sphero.RawMotorModes.FORWARD, 50, sphero.RawMotorModes.Forward, 50)
    if receivedNumber == 1:
        sphero.set_raw_motors(sphero.RawMotorModes.BACKWARD, 50, sphero.RawMotorModes.ON, 50)
    if receivedNumber == 2:
        sphero.set_raw_motors(sphero.RawMotorModes.OFF, 0, sphero.RawMotorModes.OFF, 0)

radio.on_received_number(on_recieved_number)

def on_button_pressed_a():
    radio.send_number(0)
    sphero.set_raw_motors(sphero.RawMotorModes.FORWARD, 50, sphero.RawMotorModes.Forward, 50)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(1)
    sphero.set_raw_motors(sphero.RawMotorModes.BACKWARD, 50, sphero.RawMotorModes.ON, 50)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    radio.send_number(2)
    sphero.set_raw_motors(sphero.RawMotorModes.OFF, 0, sphero.RawMotorModes.OFF, 0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)