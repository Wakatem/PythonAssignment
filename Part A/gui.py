import tkinter as tk
from tkinter import ttk
from ctypes import windll

#fix blurriness on windows
windll.shcore.SetProcessDpiAwareness(1)

#window setup
root = tk.Tk()
root.title("CSIT110 Assignment")
root.geometry("1600x940+500+400")
root.resizable(width=False, height=False)


button1 = ttk.Button(root, text="Register")
button1.pack(expand=True)

root.mainloop()