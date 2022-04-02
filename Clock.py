from tkinter import *
import time
import datetime
from tkinter.constants import CENTER, LEFT
from webbrowser import BackgroundBrowser

Applicaton_Window = Tk()
Applicaton_Window.config(bg='white')
Applicaton_Window.resizable(0, 0)
Applicaton_Window.geometry("600x350")
Applicaton_Window.title("Clock")
# Applicaton_Window.iconbitmap('/clock_g7g_icon.ico')
time_live = time.strftime("%H:%M:%p")

text_font = ("Cascadia Mono", 40, "normal")
foreground = "#737373"
background = "white"
user = "Umair"

label_1 = Label(Applicaton_Window, font=text_font,
                fg=foreground, bg=background, justify=LEFT)
label_1.grid(row=1, column=1)
label_1.pack()
label_2 = Label(Applicaton_Window, font=text_font,
                fg="#00c5f6", bg=background, justify=LEFT)
label_2.pack()
label_3 = Label(Applicaton_Window, font=text_font,
                fg=foreground, bg=background, justify=LEFT)
# label_3.grid(row=1)
label_3.pack()
label_4 = Label(Applicaton_Window, font=text_font,
                fg=foreground, bg=background, justify=LEFT)
# label_4.grid(row=2)
label_4.pack()
label_5 = Label(Applicaton_Window, font=text_font,
                fg=foreground, bg=background, justify=CENTER)
# label_5.grid(row=0, column=1)
label_5.pack()
label_6 = Label(Applicaton_Window, font=text_font,
                fg=foreground, bg=background, justify=CENTER)
# label_6.grid(row=0, column=1)
label_6.pack()
label_7 = Label(Applicaton_Window, font=text_font,
                fg=foreground, bg=background, justify=CENTER)
label_7.place(anchor=NW)
# label_7.grid(row=1, column=1)
label_7.pack()
label_8 = Label(Applicaton_Window, font=text_font,
                fg=foreground, bg=background, justify=CENTER)
# label_8.grid(row=0, column=1)
label_8.pack()


def digital_clock():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        label_1.config(text="😎")
        label_2.config(
            text="I hope you'll have a great day today.\n" + user + "\n" + time_live)
        label_2.after(200, digital_clock)

    elif hour >= 12 and hour < 17:
        label_1.config(text="🥤")
        label_2.config(text="A great noon\n" + user + "\n" + time_live)
        label_2.after(200, digital_clock)

    elif hour >= 17 and hour < 20:
        label_1.config(text="😌")
        label_2.config(text="It's evening !\n" + user + "\n" + time_live)
        label_2.after(200, digital_clock)

    else:
        label_1.config(text="🥱")
        label_2.config(text="Getting Sleepy...\n" + user + "\n" + time_live)
        label_2.after(200, digital_clock)


digital_clock()
Applicaton_Window.mainloop()
