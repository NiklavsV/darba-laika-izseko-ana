

import keyboard
import datetime

class Main:
    def __init__(self):
        pass

    def on_f13_press(self, event):
        if event.name == 'f13':
            print("f13 key was pressed!")

    def start(self):
        print("Press f13 to detect. Press ESC to stop.")
        keyboard.on_press(self.on_f13_press)

        keyboard.wait('esc')

    def stop(self):
        keyboard.unhook_all()
        print("Stopped detecting key presses.")




if __name__ == "__main__":
    main = Main()
    main.start()