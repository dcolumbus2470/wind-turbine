input.onButtonPressed(Button.A, function () {
    basic.showNumber(Revolutions)
})
input.onButtonPressed(Button.B, function () {
    elapsed_time = control.millis() - Start
    minutes = elapsed_time / 60000
    RPM = Revolutions / minutes
    basic.showNumber(RPM)
})
let RPM = 0
let minutes = 0
let elapsed_time = 0
let Start = 0
let Revolutions = 0
Revolutions = 0
Start = control.millis()
basic.forever(function () {
    if (cakLandTouch.getTap(cakLandTouch.TouchPin.P0)) {
        Revolutions += 1
        basic.pause(20)
        serial.writeValue("x", Revolutions)
        serial.writeValue("z", RPM)
    }
})
