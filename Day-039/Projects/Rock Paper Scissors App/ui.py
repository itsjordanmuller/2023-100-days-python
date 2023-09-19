from tkinter import *


class UserInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Rock Paper Scissors")

        # Paper icons created by Freepik - Flaticon
        # https://www.flaticon.com/free-icons/paper
        self.paper_img = PhotoImage(file="./images/scroll.png")

        # Rock icons created by Freepik - Flaticon
        # https://www.flaticon.com/free-icons/rock
        self.rock_img = PhotoImage(file="./images/stone.png")

        # Scissors icons created by Freepik - Flaticon
        # https://www.flaticon.com/free-icons/scissors
        self.scissors_img = PhotoImage(file="./images/scissors.png")

        self.score_canvas = Canvas(
            self.window,
            width=384,
            height=64,
            highlightthickness=0,
            borderwidth=0,
            bg="red",
        )
        self.score_canvas.grid(column=0, row=0, columnspan=3)

        self.game_canvas = Canvas(
            self.window,
            width=384,
            height=384,
            highlightthickness=0,
            borderwidth=0,
            bg="orange",
        )
        self.game_canvas.grid(column=0, row=1, columnspan=3)

        self.button_canvas = Canvas(
            self.window,
            width=384,
            height=192,
            highlightthickness=0,
            borderwidth=0,
            bg="yellow",
        )
        self.button_canvas.grid(column=0, row=2, columnspan=3)

        self.window.mainloop()
