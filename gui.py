from tkinter import *
from jsonfile import readvalue
from PIL import ImageTk, Image

# values read from .json file
tunnel = readvalue("tunnel")
azimuth = readvalue("azimuth")
acttunnel, actazimuth = 0, 0
window = Tk()
window.title("Bridge designer")

# makes window (almoast) fullscreen
window.attributes("-topmost", True)
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))

# Content starts here

frame = Frame(window, bg='grey', width=200, height=window.winfo_screenheight())
frame.grid(row=0, column=0)
frame.grid_propagate(False)

menuimage_1 = ImageTk.PhotoImage(Image.open('assets/BC-5-panel-tunnel.png').resize((132, 100), Image.LANCZOS))
menuitem_1 = Label(frame, image=menuimage_1)
menuitem_1.place(relx=0.5, rely=0.15, anchor=CENTER)

menuimage_2 = ImageTk.PhotoImage(Image.open('assets/BC-5-panel-tunnel.png').resize((132, 100), Image.LANCZOS))
menuitem_2 = Label(frame, image=menuimage_1)
menuitem_2.place(relx=0.5, rely=0.15, anchor=CENTER)

menuimage_3 = ImageTk.PhotoImage(Image.open('assets/BC-5-panel-tunnel.png').resize((132, 100), Image.LANCZOS))
menuitem_3 = Label(frame, image=menuimage_1)
menuitem_3.place(relx=0.5, rely=0.15, anchor=CENTER)

menuimage_4 = ImageTk.PhotoImage(Image.open('assets/BC-5-panel-tunnel.png').resize((132, 100), Image.LANCZOS))
menuitem_4 = Label(frame, image=menuimage_1)
menuitem_4.place(relx=0.5, rely=0.15, anchor=CENTER)

menutitle = Label(frame, text="Tunnel")
menutitle.place(relx=0.5, rely=0.05, anchor=CENTER)
# Content ends here
window.mainloop()
