from tkinter import *

tk = Tk()

info = StringVar()
info_str = "Нажата клавиша с кодом:"

def keypress(event):
    info.set(info_str + " %s" % event.keycode)

tk.title("Пример работы с клавиатурой")
tk.geometry('500x150')

label = Label(tk, textvariable=info, font=("Courier", "14"))
info.set(info_str)
label.pack()

tk.bind('<Key>', keypress)
tk.mainloop()
print("А эта строчка напечатается только тогда, когда окно программы закроют.")
