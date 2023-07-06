from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
	def __init__(self, quiz_brain: QuizBrain):
		# creating the window
		self.quiz = quiz_brain

		self.window = Tk()
		self.window.title('Quizzler')
		self.window.config(padx=20, pady=20, bg=THEME_COLOR)
		# creating the canvas
		self.canvas = Canvas(height=250, width=300, bg='white')
		self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
		self.text = self.canvas.create_text(150, 125, text="", font=("Ariel", 20, "italic"), fill=THEME_COLOR,
		                                    width=280)
		# import images
		true_image = PhotoImage(file='images/true.png')
		false_image = PhotoImage(file='images/false.png')
		# buttons
		self.true_button = Button(image=true_image, highlightthickness=0, command=self.true)
		self.true_button.grid(column=0, row=2)
		self.false_button = Button(image=false_image, highlightthickness=0, command=self.false)
		self.false_button.grid(column=1, row=2)

		# label
		self.score = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
		self.score.grid(column=1, row=0)

		self.get_next_question()

		self.window.mainloop()

	def get_next_question(self):
		if self.quiz.still_has_questions():
			self.canvas.config(bg='white')
			self.score.config(text=f'Score: {self.quiz.score}')
			q_text = self.quiz.next_question()
			self.canvas.itemconfig(self.text, text=q_text)
		else:
			self.canvas.config(bg='white')
			self.true_button.config(state='disabled')
			self.false_button.config(state='disabled')
			self.canvas.itemconfig(self.text, text=f"🎉🎉🎉🎉🎉🎉You've reached the end of the game What is the code "
			                                       f"for 🎉🎉🎉🎉🎉🎉")

	def true(self):
		self.give_feedback(self.quiz.check_answer("True"))

	def false(self):
		self.give_feedback(self.quiz.check_answer('False'))

	def give_feedback(self, is_right):
		if is_right:
			self.canvas.config(bg="green")
		else:
			self.canvas.config(bg="red")

		self.window.after(1000, self.get_next_question)

