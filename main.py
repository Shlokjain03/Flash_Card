from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}

try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("PY/Flash_Card/data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_background,image= card_front_img)
    flip_timer=window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English")
    canvas.itemconfig(card_word,text=current_card["English"])
    canvas.itemconfig(card_background,image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data=pandas.DataFrame(to_learn)
    data.to_csv("PY/Flash_Card/data/words_to_learn.csv",index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=15, pady=15, bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)

canvas = Canvas (width=700, height=426)
card_front_img = PhotoImage(file="PY/Flash_Card/images/card_front.png")
card_back_img=PhotoImage(file="PY/Flash_Card/images/card_back.png")
card_background=canvas.create_image (300, 163, image=card_front_img)
card_title=canvas.create_text(300, 150, text="", font=("Ariel", 40, "italic"))
card_word=canvas.create_text(300, 263, text="", font=("Ariel", 45, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0,columnspan=2) 

cross_image=PhotoImage(file="PY/Flash_Card/images/wrong.png")
unknow_button=Button(image=cross_image, command=next_card)
unknow_button.grid(row=1,column=0)

check_image=PhotoImage(file="PY/Flash_Card/images/right.png")
know_button=Button(image=check_image,command=next_card)
know_button.grid(row=1,column=1)

next_card()

window.mainloop()