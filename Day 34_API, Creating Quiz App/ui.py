from tkinter import *

THEME_COLOR = "#375362"
BACKGROUND_COLOR = "Grey"

class QuizInterface():

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzlers")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(text="Some Question Text: ", fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0 ,columnspan=2)

        self.canvas.create_image = PhotoImage("images/false.png")
        # self.
        self.window.mainloop()


QuizInterface()