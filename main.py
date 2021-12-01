cas = 0

def on_button_pressed_b():
    global cas
    cas = randint(250, 3000)
    music.play_tone(Note.C,cas)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_a():
    music.play_tone(Note.C,cas)
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_string("B")


def on_logo_event_pressed():
    pass
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)
