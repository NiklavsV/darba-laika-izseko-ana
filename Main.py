

import keyboard
from datetime import *

class Main:

    def __init__(self):
        self.onn = False
        pass

    def on_key_press(self, event):
        
        if event.name == 'f13':
            now = datetime.now()
            evtime = now.strftime("%Y/%m/%d %H:%M")
            self.onn = not self.onn
            print(self.onn)
            if self.onn == True:
                print(evtime)
                with open("laiki.txt", "a") as timestxt:
                    timestxt.write(evtime + 'start' + ' --- ')

            elif self.onn == False:
                print(evtime)
                with open("laiki.txt", "a") as timestxt:
                    timestxt.write(evtime + 'end' + '\n')

        
                

    def start(self):
        print("Press f13 to toggle work mode. Press ESC to stop.")
        keyboard.on_press(self.on_key_press)
        keyboard.wait('esc')
        self.stop()


    def stop(self):
        keyboard.unhook_all()
        print("Stopped detecting key presses.")




if __name__ == "__main__":
    main = Main()
    main.start()