from tkinter import *
from jsonfile import readvalue
from PIL import ImageTk, Image
cloneam = 0
# cloneamout
clones = []


def mkclone(img, x, y):
    global cloneam
    cloneam += 1
    cloneimage = ImageTk.PhotoImage(Image.open(img).resize((132, 100), Image.LANCZOS))
    cloneitem = Label(frame, image=cloneimage, bd=0, cursor="hand2")
    cloneitem.place(x=x, y=y)
    cloneitem.image = cloneimage
    cloneitem.bind("<Button-1>", lambda e: moveclone(cloneitem))
    clones.append(cloneitem)
    clones.append([x, y])


def moveclone(name):
    clonex = str(name)
    clonex = int(clonex.split("l")[2])-6
    print(clonex)


# values read from .json file
tunnel = readvalue("tunnel")
azimuth = readvalue("azimuth")
acttunnel, actazimuth = 0, 0
window = Tk()
window.title("Bridge designer")
images = ["assets/BC-5-panel-tunnel.png", 'assets/BC-5-panel-azimuth.png', 'assets/BC-5-panel-two-tunnels.png', 'assets/BC-5-panel-two-tunnels-dp.png']

# makes window (almoast) fullscreen
window.attributes("-topmost", True)
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))

# Content starts here

frame = Frame(window, bg='grey', width=200, height=window.winfo_screenheight())
frame.grid(row=0, column=0)
frame.grid_propagate(False)

menuimage_1 = ImageTk.PhotoImage(Image.open(images[0]).resize((132, 100), Image.LANCZOS))
menuitem_1 = Label(frame, image=menuimage_1, bd=0, cursor="hand2")
menuitem_1.place(relx=0.5, rely=0.15, anchor=CENTER)

menuimage_2 = ImageTk.PhotoImage(Image.open(images[1]).resize((132, 100), Image.LANCZOS))
menuitem_2 = Label(frame, image=menuimage_2, bd=0, cursor="hand2")
menuitem_2.place(relx=0.5, rely=0.3, anchor=CENTER)

menuimage_3 = ImageTk.PhotoImage(Image.open(images[2]).resize((132, 100), Image.LANCZOS))
menuitem_3 = Label(frame, image=menuimage_3, bd=0, cursor="hand2")
menuitem_3.place(relx=0.5, rely=0.45, anchor=CENTER)

menuimage_4 = ImageTk.PhotoImage(Image.open(images[3]).resize((132, 100), Image.LANCZOS))
menuitem_4 = Label(frame, image=menuimage_4, bd=0, cursor="hand2")
menuitem_4.place(relx=0.5, rely=0.6, anchor=CENTER)
menuitem_4.bind("<Button-1>", lambda e: mkclone(images[3], 100, 100))
menutitle = Label(frame, text="Control panels")
menutitle.place(relx=0.5, rely=0.05, anchor=CENTER)

# Content ends here
window.mainloop()
