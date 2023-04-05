from tkinter import *
import time
import datetime
from tkinter.constants import CENTER, LEFT

# Create the main window
Applicaton_Window = Tk()
Applicaton_Window.config(bg='white')
Applicaton_Window.resizable(0, 0)
Applicaton_Window.geometry("600x350")
Applicaton_Window.title("Clock")

# Set the initial time
time_live = time.strftime("%H:%M:%p")

# Define some style parameters
text_font = ("Cascadia Mono", 40, "normal")
foreground = "#737373"
background = "white"
user = "Umair"

# Create the labels for the clock
label_1 = Label(Applicaton_Window, font=text_font,
                fg=foreground, bg=background, justify=LEFT)
label_1.pack()
label_2 = Label(Applicaton_Window, font=text_font,
                fg="#00c5f6", bg=background, justify=LEFT)
label_2.pack()
label_3 = Label(Applicaton_Window, font=text_font,
                fg=foreground, bg=background, justify=LEFT)
label_3.pack()
label_4 = Label(Applicaton_Window, font=text_font,
                fg=foreground, bg=background, justify=LEFT)
label_4.pack()
label_5 = Label(Applicaton_Window, font=text_font,
                fg=foreground, bg=background, justify=CENTER)
label_5.pack()
label_6 = Label(Applicaton_Window, font=text_font,
                fg=foreground, bg=background, justify=CENTER)
label_6.pack()
label_7 = Label(Applicaton_Window, font=text_font,
                fg=foreground, bg=background, justify=CENTER)
label_7.pack()
label_8 = Label(Applicaton_Window, font=text_font,
                fg=foreground, bg=background, justify=CENTER)
label_8.pack()


def digital_clock():
    # Get the current hour
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        # Set the emoji and message for morning
        label_1.config(text="😎")
        label_2.config(
            text="I hope you'll have a great day today.\n" + user + "\n" + time_live)
        # Update the clock every 200 milliseconds
        label_2.after(200, digital_clock)

    elif hour >= 12 and hour < 17:
        # Set the emoji and message for noon
        label_1.config(text="🥤")
        label_2.config(text="A great noon\n" + user + "\n" + time_live)
        # Update the clock every 200 milliseconds
        label_2.after(200, digital_clock)

    elif hour >= 17 and hour < 20:
        # Set the emoji and message for evening
        label_1.config(text="😌")
        label_2.config(text="It's evening !\n" + user + "\n" + time_live)
        # Update the clock every 200 milliseconds
        label_2.after(200, digital_clock)

    else:
        # Set the emoji and message for night
        label_1.config(text="🥱")
        label_2.config(text="Getting Sleepy...\n" + user + "\n" + time_live)
        # Update the clock every 200 milliseconds
        label_2.after(200, digital_clock)


# Call the digital clock function to start the clock
digital_clock()

# Run the main loop for the window

Applicaton_Window.mainloop()
