from tkinter import *
import pandas
import random

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

data_dict = data.to_dict(orient="records") #list of dictionaries [ {row:column} ]
random_choice = random.randint(0,len(data_dict))

def next_card():
    global random_choice
    global flip_timer
    window.after_cancel(flip_timer)
    random_choice = random.randint(0,len(data_dict)-1)
    fr_word = data_dict[random_choice]["French"]
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word, text=fr_word)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    en_word = data_dict[random_choice]["English"]
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word,text=en_word)
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    data_dict.remove(data_dict[random_choice])
    print(len(data_dict))
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50 ,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# front card
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image=card_front_img)
canvas.create_image(400, 263, image=card_front_img)

#text
card_title = canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263, text="Word", font=("Arial",60,"bold"))

canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

checked_image = PhotoImage(file="images/right.png")
known_button = Button(image=checked_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
