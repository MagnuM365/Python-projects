from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=250,
            text="Some text", 
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )       #x=150, y=125, position of text in canvas and is mandotary in canvas
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_image = PhotoImage(file="images/true.png")    #always photoimage is used to import image in tkinter
        self.right_btn = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.right_btn.grid(row=2, column=0)
        
        false_image = PhotoImage(file="images/false.png")    #always photoimage is used to import image in tkinter
        self.wrong_btn = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.wrong_btn.grid(row=2, column=1)
        
        self.get_next_qn()
        
        self.window.mainloop()
    
    def get_next_qn(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Yo've reached the end of the question. Your score is {self.quiz.score}/10")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")
            self.score_label.destroy()
        
    def true_pressed(self):
        self.give_feedback( self.quiz.check_answer("True"))     #can use any method belw or this one
        
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_qn)