import datetime
import PIL
from PIL import *  # Imports the pillow library to load images into a Canvas.
from guizero import *  # Import the guizero library.
from tkinter import *  # Imports the tkinter library for the canvas.
import time  # Crucial for the terminal window.
import datetime

app = App("Hack The Brexit", height=650, width=1100)  # Create the app window, title, with height and width.

# Global Variables -----------------------------------------------------------------------------------------------------

global system_widgets

system_widgets = [".!canvas", ".!button6", ".!button7", ".!button8", ".!label"]

global data

data = []

global articles

articles = []


# ----------------------------------------------------------------------------------------------------------------------


# Functions ------------------------------------------------------------------------------------------------------------

def home_screen(user_id):
    global label
    global proceed_button
    global skip_button
    global side_tutorial

    if user_id == 1:
        print("doggo")
        # TODO: Create / update "last login" in the game save file. ("data/doggo.txt").
        # TODO: Create a "keys found" section, with each key found in the articles + overall amount.
        # TODO: Create and edit a global variable for the amount of keys found.
        # TODO: (OPTIONAL) Make an array of the keys which have been loaded from game save file.

    elif user_id == 2:
        print("cat")
    elif user_id == 3:
        print("rabbit")

    destroy_widgets()

    canvas.create_image(550, 325, image=home_background)
    side_tutorial = canvas.create_image(788, 29, image=side_bar, anchor=NW)

    validation_button = Button(text="Validation", image=validation_icon, highlightthickness=0, bd=0,
                               command=lambda: check_tutorial(1), height=46, width=46,
                               activebackground="#ffffff").place(x=8, y=263)  # Creates a validation button.

    news_button = Button(text="News Reader", image=bbc_icon, highlightthickness=0, bd=0,
                         command=lambda: check_tutorial(2), height=46, width=46,
                         activebackground="#ffffff").place(x=8, y=321)  # Creates a news reader button.

    laptop_button = Button(text="Laptop", image=boris_icon, highlightthickness=0, bd=0,
                           command=lambda: check_tutorial(3), height=46, width=46,
                           activebackground="#ffffff").place(x=8, y=380)  # Creates laptop access button.

    proceed_button = Button(text="Proceed", image=proceed_button_image, highlightthickness=0, bd=0,
                            command=proceed_tutorial, height=46, width=146,
                            activebackground="#00d639").place(x=948, y=490)  # Continues the game tutorial.

    skip_button = Button(text="Skip", image=skip_button_image, highlightthickness=0, bd=0,
                         command=lambda: check_tutorial(4), height=46, width=146,
                         activebackground="#f54242").place(x=797, y=490)  # Ignore the game tutorial.

    label = Label(app.tk)
    label.configure(text="09:00", background="black", foreground="white", font=("Courier", 14))
    label.place(x=10, y=3)

    # TODO: There should be an option to restart the game and to exit the game to main menu from the top bar.


def loading_screen():
    global terminal_box
    global lines
    global loading

    loading = Window(app, title="Boot Instance", height=650, width=1100)  # Creates the loading screen window.
    terminal_box = TextBox(loading, text="meh", height=650, width=1100, multiline=True)  # Creates textbox.
    terminal_box.tk.configure(background="black", foreground="white")  # Sets the textbox colour options.

    app.hide()  # Hides the current Main Menu.
    loading.show()  # Shows the new loading screen.

    # The following code simulates a Linux Boot Splash screen in silent mode.

    with open('resources/boot_sequence.txt', 'r') as boot_file:
        lines = [line.rstrip('\n') for line in boot_file.readlines()]

    terminal_box.repeat(10, lineDisplay)  # Change to 30!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def lineDisplay():
    terminal_lines = terminal_box.value.count('\n')  # Counts the number of lines in the terminal text box.

    if terminal_lines == 95:
        brexit_background = "resources/brexit_back.png"

        img2 = PIL.Image.open(brexit_background)
        hidden_text = text_display(img2)
        hidden_text.split()

        for word in hidden_text.split():
            data.append(str(word))

    if terminal_lines < len(lines):  # Checks if the number of terminal lines is lower
        terminal_box.append(lines[terminal_lines])
        terminal_box.tk.see('end')
    else:
        login_screen()
        loading.destroy()


def quit_game():
    sys.exit(0)  # Quit the application at any point in the game.


def destroy_widgets():
    for widget in app.tk.winfo_children():

        if str(widget) != ".!canvas":  # This statement prevents canvas from being removed.
            widget.destroy()


def countdown(count):
    label['text'] = str(datetime.timedelta(seconds=count))[2:]

    # TODO: If there are 2 keys left, decrease the countdown by one minute.
    # TODO: Give the user a warning if the "authorities" are about to approach

    if count > 0:
        app.tk.after(1000, countdown, count - 1)

    if count == 0:
        destroy_current_window()
        destroy_widgets()
        canvas.create_image(550, 325, image=game_over_screen)


def login_screen():
    app.show()

    destroy_widgets()

    canvas.create_image(550, 325, image=login_background)  # Creates login background for the login screen.

    save_slot_1 = Button(text="Save 1", image=doggo_profile, highlightthickness=0, bd=0,
                         command=lambda: home_screen(1), height=248, width=250).place(x=155, y=197)

    save_slot_2 = Button(text="Save 2", image=cat_profile, highlightthickness=0, bd=0,
                         command=lambda: home_screen(2), height=248, width=250).place(x=425, y=197)

    save_slot_3 = Button(text="Save 3", image=rabbit_profile, highlightthickness=0, bd=0,
                         command=lambda: home_screen(3), height=248, width=250).place(x=695, y=197)


def destroy_current_window():
    for widget in canvas.winfo_children():
        if ".!canvas.!canvas" in str(widget):
            widget.destroy()

    for widget in app.tk.winfo_children():

        if any(str(widget) in s for s in system_widgets):
            pass
        else:
            widget.destroy()


def text_display(source):
    width, height = source.size
    text = ""
    index = 0
    for row in range(height):
        for col in range(width):
            try:
                r, g, b = source.getpixel((col, row))
            except ValueError:
                r, g, b, a = source.getpixel((col, row))
            if row == 0 and col == 0:
                length = r
            elif index <= length:
                text += chr(r)
            index += 1
    return text


def news_reader():
    global article_number
    global news

    news = Canvas(canvas, width=975, height=585)
    news.create_image(500, 295, image=news_reader_background)
    news.place(x=85, y=47)

    news_frame = Frame(canvas, width=750, height=550)
    news_frame.place(x=290, y=82)

    news_canvas = Canvas(news_frame, scrollregion=(0, 0, 1000, 1180), width=750, height=550, )
    scrollbar_frame = Frame(news_canvas)
    news_scrollbar = Scrollbar(news_frame, orient="vertical", command=news_canvas.yview)
    news_canvas.configure(yscrollcommand=news_scrollbar.set)

    news_scrollbar.pack(side="right", fill="y")
    news_canvas.pack(side="left")
    news_canvas.create_window((0, 0), window=scrollbar_frame, anchor='nw')

    button = list()

    article_number = 0

    for r in range(4):
        for i in range(3):
            button.append(Button(scrollbar_frame, image=articles[article_number]))
            button[-1].grid(row=r, column=i)

            article_number = article_number + 1

    for button_number in range(12):
        button[button_number].configure(command=lambda button_number=button_number: open_article(button_number))

    news_home_button = Button(app.tk, text="Home", image=news_home, highlightthickness=0, bd=0,
                              command=lambda: check_tutorial(2), height=49, width=165,
                              activebackground="#f54242").place(x=109, y=270)  # Creates a Home button.

    news_favourites_button = Button(app.tk, text="Favourites", image=news_favourites, highlightthickness=0, bd=0,
                                    command=check_current_key, height=49, width=165,
                                    activebackground="#f54242").place(x=109, y=350)  # Creates a Favourites button.

    # TODO: Create a favourites window within news reader canvas.
    # TODO: Add a news "favourite" button to the full article page when article card is clicked.

    news_help_button = Button(app.tk, text="Help", image=news_help, highlightthickness=0, bd=0,
                              command=check_current_key, height=49, width=165,
                              activebackground="#f54242").place(x=109, y=429)  # Creates a Help button.

    # TODO: Create a help window within news reader canvas. The help window should explain how to find keys.


def open_article(button_order):
    # TODO: Please fix the positioning of the articles.

    article_reader = Canvas(canvas, width=750, height=550, background="#ffffff")  # Set article canvas background.
    article_reader.create_image(390, 275, image=full_articles[button_order])  # Center article image within canvas.
    article_reader.place(x=290, y=82)  # Place article canvas within news reader.

    # TODO: Create a random invisible button within the article canvas.
    # TODO: If invisible button is clicked, the user should get a "new key" notification.
    # TODO: Place "copy" button to notification. If the user clicks the copy button, the key is added to clipboard.
    # TODO: There should be an exit button if the user decides not to copy the key (key has already been found).
    # TODO: Still show the close button even if the key hasn't been found before.
    # TODO: If the same key has been found, and the user is trying to copy it again, show the warning notification.
    # TODO: Create copy and cancel buttons for the warning photo (Don't create a canvas).

    # TODO: Remove scrollbar from the side (IMPORTANT). -> Remove RHS canvas from main news reader?


def create_notification():
     canvas.create_image(297, 91, image=key_notification)


def skip_game_tutorial(button_id_1):
    if button_id_1 == 1:
        destroy_current_window()
        canvas.delete(side_tutorial)
        countdown(540)
        open_validation()

    elif button_id_1 == 2:
        destroy_current_window()
        canvas.delete(side_tutorial)
        countdown(540)
        news_reader()

    elif button_id_1 == 3:
        destroy_current_window()
        canvas.delete(side_tutorial)
        countdown(540)
        boris_laptop()

    elif button_id_1 == 4:
        destroy_current_window()
        canvas.delete(side_tutorial)
        countdown(540)
        news_reader()

    # TODO: (Optional) Create a dictionary instead of single IF statements?


def open_home_windows(button_id_1):
    if button_id_1 == 1:
        destroy_current_window()
        canvas.delete(side_tutorial)
        open_validation()

    elif button_id_1 == 2:
        destroy_current_window()
        canvas.delete(side_tutorial)
        news_reader()

    elif button_id_1 == 3:
        destroy_current_window()
        canvas.delete(side_tutorial)
        boris_laptop()

    elif button_id_1 == 4:
        destroy_current_window()
        canvas.delete(side_tutorial)
        news_reader()


def boris_laptop():
    news = Canvas(canvas, width=975, height=585)
    news.create_image(500, 295, image=boris_laptop_background)
    news.place(x=85, y=47)

    count_boris = Label(app.tk)
    count_boris.configure(text="YOU MUST FIND ALL KEYS", background="black", foreground="white", font=("Courier", 14))
    count_boris.place(x=10, y=3)

    # TODO: When opened, check in the game save file if all 7 keys have been found.
    # TODO: Display in a label how many keys have been found.
    # TODO: Once the seven keys have been found, display the "Cancel Brexit" button.


def proceed_tutorial():
    print("Proceed")

    canvas.create_image(788, 29, image=second_tutorial, anchor=NW)

    # TODO: When button clicked, display the second part of the tutorial.
    # TODO: When second part displayed, also position the "finish tutorial" button.
    # TODO: When the "finish tutorial" button is clicked, start the timer and open the news reader

    proceed_button = Button(text="Proceed", image=finish_tutorial_button, highlightthickness=0, bd=0,
                            command=lambda: check_tutorial(4), height=46, width=146,
                            activebackground="#00d639").place(x=948, y=490)


def cancel_skip():
    for widget in app.tk.winfo_children():
        if any(str(widget) in s for s in system_widgets):
            pass
        else:
            widget.destroy()


def check_tutorial(button_id):
    global warning_image
    global warning

    widgets = []

    for widget in app.tk.winfo_children():
        widgets.append(str(widget))

    if ".!button9" in widgets:  # Tutorial is active
        warning = Canvas(canvas, width=615, height=505)
        warning_image = warning.create_image(315, 255, image=warning_tutorial)
        warning.place(x=125, y=67)

        continue_game = Button(app.tk, text="Validation", image=continue_button, highlightthickness=0, bd=0,
                               command=lambda: skip_game_tutorial(button_id), height=49, width=170,
                               activebackground="#f54242").place(x=240, y=492)  # Creates a validation button.

        cancel_warning = Button(app.tk, text="Validation", image=cancel_button, highlightthickness=0, bd=0,
                                command=cancel_skip, height=49, width=170,
                                activebackground="#f54242").place(x=440, y=492)  # Creates a validation button.

    elif ".!button9" not in widgets:  # Tutorial is not active
        for widget2 in canvas.winfo_children():

            if ".!canvas.!frame" in str(widget2):
                widget2.destroy()

            if ".!canvas.!canvas" in str(widget2):
                widget2.destroy()
                destroy_current_window()
                open_home_windows(button_id)


def open_validation():
    global key_input
    global validation

    key_input = Entry(app.tk, text="meh", width=10)  # Creates textbox.
    key_input.configure(background="black", foreground="white", borderwidth=6, width=20)  # Sets textbox colours.
    key_input.place(x=822, y=316)

    check_button = Button(app.tk, text="Validation", image=check_button_image, highlightthickness=0, bd=0,
                          command=check_current_key, height=56, width=90,
                          activebackground="#f54242").place(x=840, y=492)  # Creates a validation button.

    validation = Canvas(canvas, width=895, height=505)
    validation.create_image(450, 255, image=validation_window)
    validation.place(x=125, y=67)


def check_current_key():
    if str(key_input.get()) in data:
        validation.create_image(452, 255, image=correct_image)
    else:
        validation.create_image(452, 255, image=warning_button)


# ----------------------------------------------------------------------------------------------------------------------


# Resources ------------------------------------------------------------------------------------------------------------

background_image = PhotoImage(file="resources/menu_background.png")
login_background = PhotoImage(file="resources/login_screen.png")
home_background = PhotoImage(file="resources/home_screen.png")
play_image = PhotoImage(file="resources/play_button.png")
exit_image = PhotoImage(file="resources/exit_button.png")
doggo_profile = PhotoImage(file="resources/doggo_profile.png")
cat_profile = PhotoImage(file="resources/cat_profile.png")
rabbit_profile = PhotoImage(file="resources/rabbit_profile.png")
side_bar = PhotoImage(file="resources/side_note.png")
validation_window = PhotoImage(file="resources/validation_window.png")
validation_icon = PhotoImage(file="resources/validation_icon.png")
check_button_image = PhotoImage(file="resources/check_button.png")
proceed_button_image = PhotoImage(file="resources/proceed_button.png")
skip_button_image = PhotoImage(file="resources/skip_button.png")
warning_tutorial = PhotoImage(file="resources/warning_tutorial.png")
cancel_button = PhotoImage(file="resources/cancel_button.png")
continue_button = PhotoImage(file="resources/continue_button.png")
boris_icon = PhotoImage(file="resources/boris_icon.png")
news_reader_background = PhotoImage(file="resources/news_reader.png")
bbc_icon = PhotoImage(file="resources/bbc_icon.png")
news_favourites = PhotoImage(file="resources/news_favourites.png")
news_home = PhotoImage(file="resources/news_home.png")
news_help = PhotoImage(file="resources/news_help.png")
boris_laptop_background = PhotoImage(file="resources/boris_laptop.png")
correct_image = PhotoImage(file="resources/correct_image.png")
warning_button = PhotoImage(file="resources/warning_button.png")
game_over_screen = PhotoImage(file="resources/game_over.png")
second_tutorial = PhotoImage(file="resources/second_tutorial.png")
key_notification = PhotoImage(file="resources/key_notification.png")
finish_tutorial_button = PhotoImage(file="resources/finish_tutorial.png")

# Article Files --------------------------------------------------------------------------------------------------------
anchor_article = PhotoImage(file="resources/anchor.png")
confidence_article = PhotoImage(file="resources/confidence.png")
deliver_article = PhotoImage(file="resources/deliver.png")
farmers_article = PhotoImage(file="resources/farmers.png")
fuel_article = PhotoImage(file="resources/fuel.png")
irish_article = PhotoImage(file="resources/irish.png")
letter_article = PhotoImage(file="resources/letter.png")
macron_article = PhotoImage(file="resources/macron.png")
movement_article = PhotoImage(file="resources/movement.png")
pie_article = PhotoImage(file="resources/pie.png")
touch_article = PhotoImage(file="resources/touch.png")
traffic_article = PhotoImage(file="resources/traffic.png")

anchor_full = PhotoImage(file="resources/anchor_full.png")
confidence_full = PhotoImage(file="resources/confidence_full.png")
deliver_full = PhotoImage(file="resources/deliver_full.png")
farmers_full = PhotoImage(file="resources/farmers_full.png")
fuel_full = PhotoImage(file="resources/fuel_full.png")
irish_full = PhotoImage(file="resources/irish_full.png")
letter_full = PhotoImage(file="resources/letter_full.png")
macron_full = PhotoImage(file="resources/macron_full.png")
movement_full = PhotoImage(file="resources/movement_full.png")
pie_full = PhotoImage(file="resources/pie_full.png")
touch_full = PhotoImage(file="resources/touch_full.png")
traffic_full = PhotoImage(file="resources/traffic_full.png")

articles = [anchor_article, confidence_article, deliver_article, farmers_article, fuel_article, irish_article,
            letter_article, macron_article, movement_article, pie_article, touch_article, traffic_article]

full_articles = [anchor_full, confidence_full, deliver_full, farmers_full, fuel_full, irish_full, letter_full,
                 macron_full, movement_full, pie_full, touch_full, traffic_full]

# ----------------------------------------------------------------------------------------------------------------------

canvas = Canvas(height=650, width=1100, highlightthickness=0)
canvas.place()  # Organises the canvas within the geometry manager.
canvas.create_image(550, 325, image=background_image)  # Adds the menu background to the canvas.

app.add_tk_widget(canvas)  # This adds a tweaked Tk widget to the guizero instance.

play_button = Button(text="Play", image=play_image, highlightthickness=0, bd=0, command=loading_screen,
                     height=110, width=150, activebackground="#00d639").place(x=325, y=177)  # Creates a play button.

exit_button = Button(text="Exit", image=exit_image, highlightthickness=0, bd=0, command=quit_game,
                     height=110, width=150, activebackground="#d61900").place(x=640, y=177)  # Creates a quit button.

app.display()  # This initiates the wrapped Tkinter window.
