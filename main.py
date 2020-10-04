import random, string
import tkinter as tk

class App:
	def __init__ (self, master):
		super().__init__()
		self.master = master
		self.input_val = tk.IntVar(self.master)
		self.radio_val = tk.IntVar(self.master)

		input_frame = tk.Frame(self.master)
		input_frame.pack()
		self.input_label = tk.Label(input_frame, text="Length")
		self.input_label.pack(side="left")
		self.input_entry = tk.Entry(input_frame, textvariable=self.input_val)
		self.input_entry.pack(side="right")

		SC_frame = tk.Frame(self.master)
		SC_frame.pack()
		self.SC_label = tk.Label(SC_frame, text = "Special Character?")
		self.SC_label.pack(side="left")

		SC_Radio_frame = tk.Frame(SC_frame)
		SC_Radio_frame.pack(side="right")
		self.SC_choice_yes = tk.Radiobutton(SC_Radio_frame, text= "Yes", variable = self.radio_val, value = 0)
		self.SC_choice_yes.pack(side="left")
		self.SC_choice_no = tk.Radiobutton(SC_Radio_frame, text = "No", variable = self.radio_val, value = 1)
		self.SC_choice_no.pack(side="left")

		self.button = tk.Button(self.master, text="Generate", command=self.generate)
		self.button.pack()

		self.result = tk.Label(self.master)
		self.result.pack()


	def start(self):
		self.master.mainloop()

	def generate(self):
		rand = random.SystemRandom()
		try:
			input_entry = self.input_val.get()
		except tk.TclError:
			self.result['text'] = "Invalid input value"
		else:
			if self.radio_val.get() == 0:
				alphabet = string.ascii_letters + string.digits + string.punctuation
				password = str().join(rand.choice(alphabet) for _ in range(input_entry))
				self.result['text'] = password
			elif self.radio_val.get() == 1:
				alphabet = string.ascii_letters + string.digits
				password = str().join(rand.choice(alphabet) for _ in range(input_entry))
				self.result['text'] = password

if __name__ == "__main__":
	root = tk.Tk()
	app = App(root)
	app.start()
