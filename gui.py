import tkinter.messagebox
from tkinter import *
from jsonfile import readvalue
from PIL import ImageTk, Image
global clones
clones = []


def color(tt, acttt):
    if tt != acttt:
        return "red"
    else:
        return "green"


def cls():
    res = tkinter.messagebox.askokcancel('Clear screen?', 'All unsaved progress will be lost')
    if res == 'yes':
        for clone in clones:
            delclone(clone[0], clone[1])
        clones.clear()


def validate():
    size = 19
    menuitem_5 = Label(framel, text=f"Azimuth: {thrusters[1][0]}/{thrusters[1][1]}", font=("", size), fg=color(thrusters[1][0], thrusters[1][1]), bg="grey")
    menuitem_5.place(relx=0.5, rely=0.15, anchor=CENTER)

    menuitem_9 = Label(framel, text=f"Azimuth propulsion: {thrusters[4][0]}/{thrusters[4][1]}", font=("", size), fg=color(thrusters[4][0], thrusters[4][1]), bg="grey")
    menuitem_9.place(relx=0.5, rely=0.35, anchor=CENTER)

    menuitem_6 = Label(framel, text=f"Tunnel: {thrusters[0][0]}/{thrusters[0][1]}", font=("", size), fg=color(thrusters[0][0], thrusters[0][1]), bg="grey")
    menuitem_6.place(relx=0.5, rely=0.2, anchor=CENTER, )

    menuitem_7 = Label(framel, text=f"Tunnel split handle: {thrusters[2][0]}/{thrusters[2][1]}", font=("", size), fg=color(thrusters[2][0], thrusters[2][1]), bg="grey")
    menuitem_7.place(relx=0.5, rely=0.25, anchor=CENTER)

    menuitem_8 = Label(framel, text=f"Tunnel dual screen: {thrusters[3][0]}/{thrusters[3][1]}", font=("", size), fg=color(thrusters[3][0], thrusters[3][1]), bg="grey")
    menuitem_8.place(relx=0.5, rely=0.3, anchor=CENTER, )


def mkclone(img, x, y, xs, ys, offsetx, offsety, tt):
    # tt = thruster type
    cloneimage = ImageTk.PhotoImage(Image.open(img).resize((xs, ys), Image.LANCZOS))
    cloneitem = Label(window, image=cloneimage, bd=0, cursor="fleur")
    cloneitem.place(x=x, y=y)
    cloneitem.bind("<B1-Motion>", lambda e: moveclone(cloneitem, offsetx, offsety))
    cloneitem.bind("<Button-3>", lambda e: delclone(cloneitem, tt))
    cloneitem.image = cloneimage
    if tt == "azimuth":
        thrusters[1][0] += 1
    elif tt == "tunnel":
        thrusters[0][0] += 1
    elif tt == "tunnel-split-handle":
        thrusters[2][0] += 1
    elif tt == "tunnel-dual-screen":
        thrusters[3][0] += 1
    elif tt == "azimuth-propulsion":
        thrusters[4][0] += 1
    else:
        pass
    clones.append([cloneitem, tt])
    validate()


def delclone(name, tt):
    global thrusters
    name.place_forget()
    if tt == "azimuth":
        thrusters[1][0] -= 1
    elif tt == "tunnel":
        thrusters[0][0] -= 1
    elif tt == "tunnel-split-handle":
        thrusters[2][0] -= 1
    elif tt == "tunnel-dual-screen":
        thrusters[3][0] -= 1
    elif tt == "azimuth propulsion":
        thrusters[4][0] -= 1
    else:
        pass
    validate()


def moveclone(name, offsetx, offsety):
    x, y = window.winfo_pointerxy()
    x -= window.winfo_rootx()
    y -= window.winfo_rooty()
    name.place(x=x-offsetx, y=y-offsety)


# values read from .json file
thrusters = [[0, readvalue("tunnel")], [0, readvalue("azimuth")], [0, readvalue("tunnel-split-handle")], [0, readvalue("tunnel-dual-screen")], [0, readvalue("azimuth-propulsion")]]
window = Tk()
window.title("Bridge designer")
images = ["assets/BC-5-panel-tunnel.png", 'assets/BC-5-panel-azimuth.png', 'assets/BC-5-panel-two-tunnels.png', 'assets/BC-5-panel-two-tunnels-dp.png']

# makes window (almoast) fullscreen
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
# Content starts here
window.columnconfigure(2, weight=1)
frame = Frame(window, bg='grey', width=200, height=window.winfo_screenheight())
frame.grid(row=0, column=0)
frame.grid_propagate(False)

framel = Frame(window, bg='grey', width=300, height=window.winfo_screenheight())
framel.grid(row=0, column=3)
framel.grid_propagate(False)

clsimg = ImageTk.PhotoImage(Image.open("assets/cls-light.png").resize((20, 25), Image.LANCZOS))
clsicon = Label(window, image=clsimg, bd=0, cursor="hand2")
clsicon.place(x=210, y=25)
clsicon.bind("<Button-1>", lambda e: cls())

validate()
menuimage_1 = ImageTk.PhotoImage(Image.open(images[0]).resize((132, 100), Image.LANCZOS))
menuitem_1 = Label(frame, image=menuimage_1, bd=0, cursor="hand2")
menuitem_1.place(relx=0.5, rely=0.3, anchor=CENTER)
menuitem_1.bind("<Button-1>", lambda e: mkclone(images[0], 40, 170, 132, 100, 70, 50, "tunnel"))
menutitle = Label(frame, text="Control panels", font=("", 16))
menutitle.place(relx=0.5, rely=0.05, anchor=CENTER)
menutitle = Label(framel, text="Thruster types", font=("", 16))
menutitle.place(relx=0.5, rely=0.05, anchor=CENTER)

menuimage_2 = ImageTk.PhotoImage(Image.open(images[1]).resize((132, 100), Image.LANCZOS))
menuitem_2 = Label(frame, image=menuimage_2, bd=0, cursor="hand2")
menuitem_2.place(relx=0.5, rely=0.15, anchor=CENTER)
menuitem_2.bind("<Button-1>", lambda e: mkclone(images[1], 40, 66, 132, 100, 70, 50, "azimuth"))

menuimage_3 = ImageTk.PhotoImage(Image.open(images[2]).resize((132, 100), Image.LANCZOS))
menuitem_3 = Label(frame, image=menuimage_3, bd=0, cursor="hand2")
menuitem_3.place(relx=0.5, rely=0.45, anchor=CENTER)
menuitem_3.bind("<Button-1>", lambda e: mkclone(images[2], 40, 280, 132, 100, 70, 50, "tunnel-split-handle"))

menuimage_4 = ImageTk.PhotoImage(Image.open(images[3]).resize((183, 100), Image.LANCZOS))
menuitem_4 = Label(frame, image=menuimage_4, bd=0, cursor="hand2")
menuitem_4.place(relx=0.5, rely=0.6, anchor=CENTER)
menuitem_4.bind("<Button-1>", lambda e: mkclone(images[3], 20, 390, 183, 100, 92.5, 50, "tunnel-dual-screen"))

# Content ends here
window.mainloop()
