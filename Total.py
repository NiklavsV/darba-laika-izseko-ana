import keyboard



class aggregate:
    def __init__(self):
        pass

    def on_key_press(self, event):
        
        if event.name == 'f14':
            with open("laiki.txt","r") as Timefile:
                current_date = None
                date_hours = 0
                for line in Timefile:
                    parts = line.strip().split()
                    this_date = parts[0]
                    these_hours = parts[-1]

                    if this_date == current_date:
                        date_hours += these_hours
                    
                    elif current_date == None:
                        current_date = this_date
                        date_hours = these_hours
                    
                    else:
                        with open('stundas.txt', 'a') as hours_file:
                            hours_file.write(f'datums {current_date} - stundas {date_hours} \n')
                        date_hours = 0
                        current_date = this_date
                if current_date is not None:
                    with open('stundas.txt', 'a') as hours_file:
                        hours_file.write(f'datums {current_date} - stundas {date_hours}\n')



    def start(self):
        print("Press f14 to calculate work hours.")
        keyboard.on_press(self.on_key_press)
        keyboard.wait('esc')
        self.stop()


    def stop(self):
        keyboard.unhook_all()
        print("Stopped detecting key presses.")

main = aggregate()
main.start()