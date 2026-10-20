import tkinter as tk
import random
from threading import Thread
from playsound import playsound 

def music():
    playsound('music.mp3')

Thread(target = music, daemon=True).start()

window = tk.Tk()
window.title('Dota 2 KeyGen')
window.geometry('500x400')
window.resizable(0, 0)
bg_img = tk.PhotoImage(file='dota2.png')

label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)


symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',\
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',\
            'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [i for i in range(1, 28)]

def cancel():
    window.destroy()

def generate():
    key = ""
    first_p = ""
    first_part = numbers[symbols.index(random.choice(symbols[:14]))+1]
    third_part = numbers[symbols.index(random.choice(symbols[14:]))+1]
    if first_part < third_part:
        if first_part < 10:
            first_p = '0'+str(first_part)
        else:
            first_p = str(first_part)
        second_part = random.choices(symbols, k=7)
        s = 0
        for i in range(len(second_part)):
            if first_part < numbers[symbols.index(second_part[i])+1] < third_part:
                s += 1
        
        while s != 7:
            second_part = random.choices(symbols, k=7)
            s = 0
            for i in range(len(second_part)):
                if first_part < numbers[symbols.index(second_part[i])+1] < third_part:
                    s += 1

        key=f"{first_p} {''.join(map(str, second_part))} {str(third_part)}"
        output_label.config(text=key)



output_label = tk.Label(window, 
                        width=20, 
                        height=3)
output_label.pack(pady=150)


button_generate = tk.Button(window, 
                    text="Generate Key", 
                    width=15,
                    command=generate)
button_generate.place(relx=0.333, rely=0.6)

button_cancel = tk.Button(window,
                          width=5,
                          text="Close", 
                          command=cancel)
button_cancel.place(relx=0.41, rely=0.9)

window.mainloop()