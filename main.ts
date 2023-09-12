// import time
radio.setGroup(10)
radio.onReceivedNumber(function on_recieved_number(receivedNumber: number) {
    if (receivedNumber == 0) {
        basic.showArrow(ArrowNames.East)
        sphero.setRawMotors(sphero.RawMotorModes.backward, 50, sphero.RawMotorModes.forward, 50)
    }
    
    if (receivedNumber == 1) {
        basic.showArrow(ArrowNames.West)
        sphero.setRawMotors(sphero.RawMotorModes.forward, 50, sphero.RawMotorModes.backward, 50)
    }
    
    if (receivedNumber == 2) {
        basic.showArrow(ArrowNames.North)
        sphero.setRawMotors(sphero.RawMotorModes.forward, 100, sphero.RawMotorModes.forward, 100)
    }
    
    if (receivedNumber == 3) {
        basic.showArrow(ArrowNames.South)
        sphero.setRawMotors(sphero.RawMotorModes.backward, 50, sphero.RawMotorModes.backward, 50)
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendNumber(0)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendNumber(1)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    radio.sendNumber(2)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    radio.sendNumber(3)
    
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
