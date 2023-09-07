// import time
radio.setGroup(10)
radio.onReceivedNumber(function on_recieved_number(receivedNumber: number) {
    if (receivedNumber == 0) {
        basic.showIcon(IconNames.Happy)
        sphero.setRawMotors(sphero.RawMotorModes.forward, 100, sphero.RawMotorModes.backward, 100)
    }
    
    if (receivedNumber == 1) {
        basic.showIcon(IconNames.Sad)
        sphero.setRawMotors(sphero.RawMotorModes.backward, 100, sphero.RawMotorModes.forward, 100)
    }
    
    if (receivedNumber == 2) {
        basic.showIcon(IconNames.Asleep)
        sphero.setRawMotors(sphero.RawMotorModes.forward, 100, sphero.RawMotorModes.forward, 100)
    }
    
    if (receivedNumber == 3) {
        basic.showIcon(IconNames.Giraffe)
        sphero.wake()
    }
    
})
//     sphero.set_raw_motors(sphero.RawMotorModes.FORWARD, 100, sphero.RawMotorModes.FORWARD, 100)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendNumber(0)
})
//     sphero.set_raw_motors(sphero.RawMotorModes.BACKWARD, 100, sphero.RawMotorModes.BACKWARD, 100)
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendNumber(1)
})
//     sphero.set_raw_motors(sphero.RawMotorModes.OFF, 0, sphero.RawMotorModes.OFF, 0)
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    radio.sendNumber(2)
})
basic.forever(function on_forever() {
    if (input.lightLevel() == 0) {
        sphero.setRgbLedByIndex(sphero.LEDs.rightHeadlight, 255, 255, 255)
        sphero.setRgbLedByIndex(sphero.LEDs.leftHeadlight, 255, 255, 255)
        sphero.setRgbLedByIndex(sphero.LEDs.rightBrakelight, 255, 0, 0)
        sphero.setRgbLedByIndex(sphero.LEDs.leftBrakelight, 255, 0, 0)
    } else {
        sphero.setAllLeds(0, 0, 0)
    }
    
})
