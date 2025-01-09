
#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk
import tkinter.font as tkFont

# main window
root = tk.Tk()
root.wm_geometry("200x200")

#Create empty frame(new window for components in root)
frame_login = tk.Frame(root)


#activate the gird in our new frame
frame_login.grid()

#widgets for frame_login
normal_font = tkFont.Font(family="Ariel", size=10, weight="bold")
lbl_username = tk.Label(frame_login, text='Username:', font=normal_font, fg='red')
lbl_username.pack()

#text box for username
entry_username = tk.Entry(frame_login, bd=3)
entry_username.pack()
root.mainloop()

