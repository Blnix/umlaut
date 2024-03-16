from playsound import playsound
import threading
import keyboard

umlauts = {
  "ae": "ä",
  "ue": "ü",
  "oe": "ö",
  "AE": "Ä",
  "UE": "Ü",
  "OE": "Ö",
  "ss": "ß",
  "ee": "é"
}

#Visit https://github.com/boppreh/keyboard?tab=readme-ov-file#keyboardall_modifiers
#to get the name of special keys.

key_to_pause = "scroll lock"
play_activation_sound = True


key_buffer = []
paused = False

def on_key_event(event):
    global paused
    if not paused:
        global key_buffer
        if event.event_type == keyboard.KEY_UP:                
            key_buffer.append(event.name)

            if len(key_buffer) == 1:
                return
            while len(key_buffer) > 2:
                del key_buffer[0]
                
            lookup_text = key_buffer[0] + key_buffer[1]
            if lookup_text in umlauts:
                keyboard.press_and_release("backspace")
                keyboard.press_and_release("backspace")

                keyboard.write(umlauts[lookup_text])
                key_buffer = []

def pausefunction():
    global paused,play_activation_sound
    if play_activation_sound and paused:
        threading.Thread(target=playsound, args=("start.mp3",)).start()
    elif play_activation_sound and not paused:
        threading.Thread(target=playsound, args=("stop.mp3",)).start()
    paused = not paused

keyboard.hook(on_key_event)
keyboard.add_hotkey(key_to_pause, pausefunction)
keyboard.wait()