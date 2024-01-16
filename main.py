def on_button_pressed_a():
    basic.show_number(Revolutions)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global elapsed_time, minutes, RPM
    elapsed_time = control.millis() - Start
    minutes = elapsed_time / 60000
    RPM = Revolutions / minutes
    basic.show_number(RPM)
input.on_button_pressed(Button.B, on_button_pressed_b)

RPM = 0
minutes = 0
elapsed_time = 0
Start = 0
Revolutions = 0
Revolutions = 0
Start = control.millis()

def on_forever():
    global Revolutions
    if cakLandTouch.get_tap(cakLandTouch.TouchPin.P0):
        Revolutions += 1
        basic.pause(20)
basic.forever(on_forever)
