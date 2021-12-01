let cas = 0
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    cas = randint(250, 3000)
    music.playTone(Note.C, cas)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music.playTone(Note.C, cas)
})
basic.showString("B")
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    
})
