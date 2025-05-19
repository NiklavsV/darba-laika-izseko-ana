
#import keyboard
#
#class Main():
#
#    event = keyboard.hook()
#
#    if event.event_type == 'down' and event.name == 'F':
#        print("f")
#    

import keyboard
import time

class Main:
    def __init__(self):
        self.running = False

    def on_f13_press(self, event):
        if event.name == 'f13':
            print("f13 key was pressed!")

    def start(self):
        self.running = True
        print("Press f13 to detect. Press ESC to stop.")
        keyboard.on_press(self.on_f13_press)

        keyboard.wait('esc')

    def stop(self):
        self.running = False
        keyboard.unhook_all()
        print("Stopped detecting key presses.")




if __name__ == "__main__":
    main = Main()
    main.start()