import tkinter.messagebox
import tkinter.filedialog
from tkinter import *
from jsonfile import readvalue
from PIL import ImageTk, Image
import mss

global clones, screenless
screenless = 0
clones = []
screens = False


def color(acttt, tt):
    if tt == 0 and acttt == 0:
        return "black"
    elif (tt != acttt and tt != "Max:1") or (tt == "Max:1" and acttt > 1):
        return "red"
    else:
        return "green"


def cls():
    global screenless
    if tkinter.messagebox.askokcancel('Clear screen?', 'All unsaved progress will be lost'):
        for clone in clones:
            delclone(clone[0], clone[1], clone[2])
        clones.clear()
        for i in thrusters:
            i[0] = 0
        screenless = 0
        validate()


def validate():
    global menucounter_4
    size = 18
    try:
        menucounter_4.place_forget()
    except NameError:
        pass
    menucounter_1 = Label(framel, text=f"Azimuth: {thrusters[0][0]}/{thrusters[1][1]}", font=("", size), fg=color(thrusters[0][0], thrusters[0][1]), bg="grey")
    menucounter_1.place(relx=0.5, rely=0.15, anchor=CENTER)

    menucounter_2 = Label(framel, text=f"Tunnel: {thrusters[1][0]}/{thrusters[1][1]}", font=("", size), fg=color(thrusters[1][0], thrusters[1][1]), bg="grey")
    menucounter_2.place(relx=0.5, rely=0.2, anchor=CENTER, )

    menucounter_3 = Label(framel, text=f"split handle: {thrusters[2][0]}/{thrusters[2][1]}", font=("", size), fg=color(thrusters[2][0], thrusters[2][1]), bg="grey")
    menucounter_3.place(relx=0.5, rely=0.25, anchor=CENTER)

    menucounter_4 = Label(framel, text=f"screen: {thrusters[3][0]}/{thrusters[3][1]}", font=("", size), fg=color(thrusters[3][0], thrusters[3][1]), bg="grey")
    menucounter_4.place(relx=0.5, rely=0.3, anchor=CENTER)


def mkclone(img, x, y, xs, ys, offsetx, offsety, tt, screen):
    # tt = thruster type
    global screenless
    cloneimage = ImageTk.PhotoImage(Image.open(img).resize((xs, ys), Image.LANCZOS))
    cloneitem = Label(window, image=cloneimage, bd=0, cursor="fleur")
    cloneitem.place(x=x, y=y)
    cloneitem.bind("<B1-Motion>", lambda e: moveclone(cloneitem, offsetx, offsety))
    cloneitem.bind("<Button-3>", lambda e: delclone(cloneitem, tt, screen))
    cloneitem.image = cloneimage
    thrusters[tt][0] += 1
    if not screen:
        thrusters[3][1] = 1
        screenless += 1
    if tt == 2:
        thrusters[1][0] += 2
    clones.append([cloneitem, tt, screen])
    validate()


def export(root):
    default_file_name = "Bridgedesign.png"
    file_name = tkinter.filedialog.asksaveasfilename(defaultextension=".png", initialfile=default_file_name)
    if file_name:
        root.lift()  # Raise the window to the top of the stacking order
        root.update()  # Refresh the state of the window
        x = root.winfo_x()
        y = root.winfo_y()
        width = root.winfo_width()
        height = root.winfo_height()
        offset = 210
        with mss.mss() as sct:
            sct_img = sct.grab({"left": x+offset, "top": y+30, "width": width-503, "height": height-80})

        mss_img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        mss_img.save(file_name)


def delclone(name, tt, screen):
    global screenless
    name.place_forget()
    thrusters[tt][0] -= 1
    if tt == 2:
        thrusters[1][0] -= 2
    if not screen:
        screenless -= 1
    if screenless < 1:
        thrusters[3][1] = "Max:1"
    validate()


def moveclone(name, offsetx, offsety):
    x, y = window.winfo_pointerxy()
    x -= window.winfo_rootx()
    y -= window.winfo_rooty()
    name.place(x=x-offsetx, y=y-offsety)


# values read from .json file
thrusters = list(readvalue())

window = Tk()
window.title("Bridge designer")

images = ["assets/BC-5-panel-tunnel.png", 'assets/BC-5-panel-azimuth.png', 'assets/BC-5-panel-two-tunnels.png', 'assets/BC-5-panel-two-tunnels-dp.png', "assets/BC-5-panel-azimuth-wo-monitor.png", "assets/BC-5-panel-tunnel-wo-monitor.png", "assets/BC-5-panel-two-tunnels-wo-monitor.png", "assets/BC-5-common-monitor.png"]

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


clsimg = ImageTk.PhotoImage(Image.open("assets/cls dark.png").resize((20, 25), Image.LANCZOS))
clsicon = Label(window, image=clsimg, bd=0, cursor="hand2", bg="grey")
clsicon.place(x=175, y=25)
clsicon.bind("<Button-1>", lambda e: cls())

menutitle = Label(framel, text="Thruster types", font=("", 16))
menutitle.place(relx=0.5, rely=0.05, anchor=CENTER)

menutitle = Label(frame, text="Control panels", font=("", 16))
menutitle.place(relx=0.5, rely=0.05, anchor=CENTER)

exportimg = ImageTk.PhotoImage(Image.open("assets/export.png").resize((30, 30), Image.LANCZOS))
exporticon = Label(framel, image=exportimg, bd=0, bg="grey",  cursor="hand2")
exporticon.place(anchor=CENTER, relx=0.1, rely=0.05)
exporticon.bind("<Button-1>", lambda e: export(window))


def switch():
    global screens, menuitem_1, menuitem_2, menuitem_3, menuitem_4, menuitem_8
    try:
        menuitem_8.place_forget()
    except NameError:
        pass
    if screens := not screens:
        menuimage_1 = ImageTk.PhotoImage(Image.open(images[0]).resize((132, 100), Image.LANCZOS))
        menuitem_1 = Label(frame, image=menuimage_1, bd=0, cursor="hand2")
        menuitem_1.place(relx=0.5, rely=0.3, anchor=CENTER)
        menuitem_1.bind("<Button-1>", lambda e: mkclone(images[0], 40, 170, 132, 100, 70, 50, 1, True))
        menuitem_1.image = menuimage_1

        menuimage_2 = ImageTk.PhotoImage(Image.open(images[1]).resize((132, 100), Image.LANCZOS))
        menuitem_2 = Label(frame, image=menuimage_2, bd=0, cursor="hand2")
        menuitem_2.place(relx=0.5, rely=0.15, anchor=CENTER)
        menuitem_2.bind("<Button-1>", lambda e: mkclone(images[1], 40, 66, 132, 100, 70, 50, 0, True))
        menuitem_2.image = menuimage_2

        menuimage_3 = ImageTk.PhotoImage(Image.open(images[2]).resize((132, 100), Image.LANCZOS))
        menuitem_3 = Label(frame, image=menuimage_3, bd=0, cursor="hand2")
        menuitem_3.place(relx=0.5, rely=0.45, anchor=CENTER)
        menuitem_3.bind("<Button-1>", lambda e: mkclone(images[2], 40, 280, 132, 100, 70, 50, 2, True))
        menuitem_3.image = menuimage_3

        menuimage_4 = ImageTk.PhotoImage(Image.open(images[3]).resize((183, 100), Image.LANCZOS))
        menuitem_4 = Label(frame, image=menuimage_4, bd=0, cursor="hand2")
        menuitem_4.place(relx=0.5, rely=0.6, anchor=CENTER)
        menuitem_4.bind("<Button-1>", lambda e: mkclone(images[3], 20, 390, 183, 100, 92.5, 50, 2, True))
        menuitem_4.image = menuimage_4

        nextimg = ImageTk.PhotoImage(Image.open("assets/navarrow.png").resize((40, 40), Image.LANCZOS))
        nextpage = Label(frame, image=nextimg, bd=0, cursor="hand2", bg="grey")
        nextpage.bind("<Button-1>", lambda e: switch())
        nextpage.place(relx=0.4, rely=0.75)
        nextpage.image = nextimg
    else:
        menuitem_1.place_forget(), menuitem_2.place_forget(), menuitem_3.place_forget(), menuitem_4.place_forget()

        menuimage_5 = ImageTk.PhotoImage(Image.open(images[4]).resize((84, 100), Image.LANCZOS))
        menuitem_5 = Label(frame, image=menuimage_5, bd=0, cursor="hand2")
        menuitem_5.place(relx=0.5, rely=0.15, anchor=CENTER)
        menuitem_5.bind("<Button-1>", lambda e: mkclone(images[4], 60, 66, 84, 100, 43, 50, 0, False))
        menuitem_5.image = menuimage_5

        menuimage_6 = ImageTk.PhotoImage(Image.open(images[5]).resize((84, 100), Image.LANCZOS))
        menuitem_6 = Label(frame, image=menuimage_6, bd=0, cursor="hand2")
        menuitem_6.place(relx=0.5, rely=0.3, anchor=CENTER)
        menuitem_6.bind("<Button-1>", lambda e: mkclone(images[5], 60, 170, 84, 100, 43, 50, 1, False))
        menuitem_6.image = menuimage_6

        menuimage_7 = ImageTk.PhotoImage(Image.open(images[6]).resize((84, 100), Image.LANCZOS))
        menuitem_7 = Label(frame, image=menuimage_7, bd=0, cursor="hand2")
        menuitem_7.place(relx=0.5, rely=0.45, anchor=CENTER)
        menuitem_7.bind("<Button-1>", lambda e: mkclone(images[6], 60, 280, 84, 100, 43, 50, 2, False))
        menuitem_7.image = menuimage_7

        menuimage_8 = ImageTk.PhotoImage(Image.open(images[7]).resize((102, 150), Image.LANCZOS))
        menuitem_8 = Label(frame, image=menuimage_8, bd=0, cursor="hand2")
        menuitem_8.place(relx=0.5, rely=0.63, anchor=CENTER)
        menuitem_8.bind("<Button-1>", lambda e: mkclone(images[7], 60, 390, 136, 200, 67, 100, 3, True))
        menuitem_8.image = menuimage_8

        nextimg = ImageTk.PhotoImage(Image.open("assets/navarrow.png").resize((40, 40), Image.LANCZOS).rotate(180))
        nextpage = Label(frame, image=nextimg, bd=0, cursor="hand2", bg="grey")
        nextpage.bind("<Button-1>", lambda e: switch())
        nextpage.place(relx=0.4, rely=0.75)
        nextpage.image = nextimg


switch()
validate()
# Content ends here
window.mainloop()
