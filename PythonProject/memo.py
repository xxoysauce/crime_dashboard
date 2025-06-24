from tkinter import *
from tkinter.filedialog import *

def new_file():
    text_area.delete(1.0, END)

def save_file():
    f =asksaveasfile(mode="w", defaultextension=".txt",filetypes=[("text files", ".txt")])
    text_save = str(text_area.get(1.0, END))
    f.write(text_save)
    f.close()

def maker():
    help_view=Toplevel()
    help_view.geometry("300x50")
    help_view.title("PD")
    lb = Label(help_view, text="Who make this~!")
    lb.pack()

window = Tk()
window.title("Notepad")
window.geometry("400x400")
window.resizable(False, False)

menu = Menu(window)
menu_1 = Menu(menu, tearoff=0)
menu_1.add_command(label='new file')
menu_1.add_command(label='save')
menu_1.add_separator()
menu_1.add_command(label='quit',command=window.destroy)
menu.add_cascade(label='file', menu=menu_1)

menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label='PD')
menu.add_cascade(label='PD', menu=menu_2)

text_area = Text(window)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text_area.grid(sticky=N + E + S + W)

window.config(menu=menu)

window.mainloop()



