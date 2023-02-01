from tkinter import *
from jsonfile import readvalue
from PIL import ImageTk, Image


def mkclone(img, x, y, xs, ys, offsetx, offsety, tt, amount):
    # tt = thruster type
    global actazimuth, acttunnel
    cloneimage = ImageTk.PhotoImage(Image.open(img).resize((xs, ys), Image.LANCZOS))
    cloneitem = Label(window, image=cloneimage, bd=0, cursor="fleur")
    cloneitem.place(x=x, y=y)
    cloneitem.bind("<B1-Motion>", lambda e: moveclone(cloneitem, offsetx, offsety))
    cloneitem.bind("<Button-3>", lambda e: delclone(cloneitem, tt, amount))
    cloneitem.image = cloneimage
    if tt == "azimuth":
        actazimuth += amount
    elif tt == "tunnel":
        acttunnel += amount
    else:
        pass
    print(actazimuth, acttunnel)


def delclone(name, tt, amount):
    global acttunnel, actazimuth, acttunnel, actazimuth
    name.place_forget()
    if tt == "azimuth":
        actazimuth -= amount
    elif tt == "tunnel":
        acttunnel -= amount
    else:
        pass
    print(actazimuth, acttunnel)


def moveclone(name, offsetx, offsety):
    x, y = window.winfo_pointerxy()
    x -= window.winfo_rootx()
    y -= window.winfo_rooty()
    name.place(x=x-offsetx, y=y-offsety)


# values read from .json file
tunnel = readvalue("tunnel")
azimuth = readvalue("azimuth")
acttunnel, actazimuth = 0, 0
window = Tk()
window.title("Bridge designer")
images = ["assets/BC-5-panel-tunnel.png", 'assets/BC-5-panel-azimuth.png', 'assets/BC-5-panel-two-tunnels.png', 'assets/BC-5-panel-two-tunnels-dp.png']

# makes window (almoast) fullscreen
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))

# Content starts here

frame = Frame(window, bg='grey', width=200, height=window.winfo_screenheight())
frame.grid(row=0, column=0)
frame.grid_propagate(False)

menuimage_1 = ImageTk.PhotoImage(Image.open(images[0]).resize((132, 100), Image.LANCZOS))
menuitem_1 = Label(frame, image=menuimage_1, bd=0, cursor="hand2")
menuitem_1.place(relx=0.5, rely=0.15, anchor=CENTER)
menuitem_1.bind("<Button-1>", lambda e: mkclone(images[0], 40, 66, 132, 100, 70, 50, "tunnel", 1))
menutitle = Label(frame, text="Control panels")
menutitle.place(relx=0.5, rely=0.05, anchor=CENTER)

menuimage_2 = ImageTk.PhotoImage(Image.open(images[1]).resize((132, 100), Image.LANCZOS))
menuitem_2 = Label(frame, image=menuimage_2, bd=0, cursor="hand2")
menuitem_2.place(relx=0.5, rely=0.3, anchor=CENTER)
menuitem_2.bind("<Button-1>", lambda e: mkclone(images[1], 40, 170, 132, 100, 70, 50, "azimuth", 1))

menuimage_3 = ImageTk.PhotoImage(Image.open(images[2]).resize((132, 100), Image.LANCZOS))
menuitem_3 = Label(frame, image=menuimage_3, bd=0, cursor="hand2")
menuitem_3.place(relx=0.5, rely=0.45, anchor=CENTER)
menuitem_3.bind("<Button-1>", lambda e: mkclone(images[2], 40, 280, 132, 100, 70, 50, "tunnel", 2))

menuimage_4 = ImageTk.PhotoImage(Image.open(images[3]).resize((183, 100), Image.LANCZOS))
menuitem_4 = Label(frame, image=menuimage_4, bd=0, cursor="hand2")
menuitem_4.place(relx=0.5, rely=0.6, anchor=CENTER)
menuitem_4.bind("<Button-1>", lambda e: mkclone(images[3], 20, 390, 183, 100, 92.5, 50, "tunnel", 2))

# Content ends here
window.mainloop()
