import keyboard



class aggregate:
    def __init__(self):
        pass

    def on_key_press(self, event):
        
        if event.name == 'f14':
            with open("laiki.txt","r") as Timefile:

                pass



    def start(self):
        print("Press f14 to calculate work hours.")
        keyboard.on_press(self.on_key_press)
        keyboard.wait('esc')
        self.stop()


    def stop(self):
        keyboard.unhook_all()
        print("Stopped detecting key presses.")

aggregate.start()