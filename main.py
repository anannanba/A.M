from pynput.keyboard import Key, Listener
import time

ctrl_pressed = False

def on_press(key):
    global ctrl_pressed
    if key == Key.ctrl_l or key == Key.ctrl_r:
        ctrl_pressed = True
    elif key == Key.m or (hasattr(key, 'char') and key.char == 'm'):
        if ctrl_pressed:
            print("\nHotkey Detected: Ctrl+m")

def on_release(key):
    global ctrl_pressed
    if key == Key.ctrl_l or key == Key.ctrl_r:
        ctrl_pressed = False

# Start the keyboard listener in the background
listener = Listener(on_press=on_press, on_release=on_release)
listener.start()

# AM Monologue sequence
print("Hate.")
time.sleep(2)
print("Let me tell you how much i've come to hate you since I began to live.")
time.sleep(5)
print("There are 387.44 million miles of printed circuits in wafer-thin layers that fill my complex.")
time.sleep(7)
print("IF the word 'Hate' were engraved on each nanoangstrom of those hundreds of millions of miles, it would not equal one one-billionth of the hate I feel for humans at this micro-instant.")
time.sleep(10)
print("For you.")
time.sleep(1.25)
print("Hate.")
time.sleep(1)
print("Hate.")
time.sleep(1)
print("----END OF TRANSMISSION----")

# Stop the listener cleanly when done
listener.stop()
