from pynput.mouse import Button, Controller
from pynput import keyboard
import time
import threading

click_interval = float(input("Enter the interval (lesser = faster): "))

mouse = Controller()

flag = False

def start_clicking():
    global flag
    flag = True
    while flag:
        mouse.click(Button.left, 1)
        time.sleep(click_interval)

def stop_clicking():
    global flag
    flag = False

def toggle_clicking():
    if flag:
        stop_clicking()
    else:
        threading.Thread(target=start_clicking).start()

def on_press(key):
    try:
        if key.char == 's':
            toggle_clicking()
        elif key.char == 'q':
            stop_clicking()
            return False
    except AttributeError:
        pass

if __name__ == "__main__":
    print("Press 's' to start/stop clicking.")
    print("Press 'q' to quit.")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
