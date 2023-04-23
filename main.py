import tkinter as tk
from tkinter.ttk import *
import random

window = tk.Tk()
window.title('Passcode Generator')
window.geometry('450x350')
window.configure(bg='#F5DEB3')
window.resizable(0,0)
lbl = Label(window,text="Passcode Generator", font=('Times New Roman',28))
lbl.configure(background='#F5DEB3')
pass_show = Entry(window,width=30,font=36)
pass_show.insert(0,"Click 'Generate'")
lbl.place(relx=0.5,y=50,anchor='center')
pass_show.place(relx=0.5,y=150,anchor='center')

def generate():
    pass_show.delete(0,'end')
    list_pass = ['1','2','3','4','5','6','7','8','9','0','@','$','&','q','w','e','r','t','y','u','i','o',
                 'p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T',
                 'Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','#']

    passw = ''
    numb = random.randint(8,16)
    for i in range(numb):
        list_word = random.choice(list_pass)
        passw+=list_word

    pass_show.insert(0,passw)

btn_gen = tk.Button(window,text="Generate",command=generate)
btn_gen.place(x=190,y=230)

window.mainloop()



