import random, string, sys
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont

class App:
	def __init__ (self, master):
		# super().__init__()
		self.master = master
		self.input_val = tk.IntVar(self.master)
		self.SC_radio_val = tk.BooleanVar(self.master)
		self.UC_radio_val = tk.BooleanVar(self.master)
		self.NC_radio_val = tk.BooleanVar(self.master)
		fontStyle = tkFont.Font(family="Helvetica", size=30, weight="bold")
		fontStyle2 = tkFont.Font(family="Helvetica", size=20, weight="bold")

		title_frame = tk.Frame(self.master)
		title_frame.config(background = "#292C4D")
		title_frame.pack()
		self.title_label = tk.Label(title_frame, text = "Password Generator", font=fontStyle)
		self.title_label.config(background = "#292C4D", foreground="#ff8080")
		self.title_label.pack(side="left", pady=30)

		input_frame = tk.Frame(self.master)
		input_frame.config(background = "#292C4D")
		input_frame.pack()
		self.input_label = tk.Label(input_frame, text="Length")
		self.input_label.config(background = "#292C4D", foreground="#ff8080")
		self.input_label.pack(side="left",padx=20, pady=10)
		self.input_entry = tk.Entry(input_frame, textvariable=self.input_val)
		self.input_entry.bind("<Return>", self.generate)
		self.input_entry.pack(side="left", padx=20, pady=10)

		SC_frame = tk.Frame(self.master)
		SC_frame.config(background = "#292C4D")
		SC_frame.pack()
		self.SC_label = tk.Label(SC_frame, text = "Special Character")
		self.SC_label.config(background = "#292C4D", foreground="#ff8080")
		self.SC_label.pack(side="left", padx=20, pady=5)

		SC_Radio_frame = tk.Frame(SC_frame)
		SC_Radio_frame.config(background = "#292C4D")
		SC_Radio_frame.pack(side="left")
		self.SC_choice_yes = tk.Radiobutton(SC_Radio_frame, text= "Yes", variable = self.SC_radio_val, value = True)
		self.SC_choice_yes.config(background = "#292C4D",foreground="#ff8080")
		self.SC_choice_yes.pack(side="left")
		self.SC_choice_no = tk.Radiobutton(SC_Radio_frame, text = "No", variable = self.SC_radio_val, value = False)
		self.SC_choice_no.config(background = "#292C4D", foreground="#ff8080")
		self.SC_choice_no.pack(side="left")

		UC_frame = tk.Frame(self.master)
		UC_frame.config(background = "#292C4D")
		UC_frame.pack()
		self.UC_label = tk.Label(UC_frame, text = "Upper Case Alphabet")
		self.UC_label.config(background = "#292C4D", foreground="#ff8080")
		self.UC_label.pack(side="left", padx=20, pady=5)

		UC_Radio_frame = tk.Frame(UC_frame)
		UC_Radio_frame.config(background = "#292C4D")
		UC_Radio_frame.pack(side="left")
		self.UC_choice_yes = tk.Radiobutton(UC_Radio_frame, text = "Yes", variable = self.UC_radio_val, value = True)
		self.UC_choice_yes.config(background = "#292C4D",foreground="#ff8080")
		self.UC_choice_yes.pack(side="left")
		self.UC_choice_no = tk.Radiobutton(UC_Radio_frame, text = "No", variable = self.UC_radio_val, value = False)
		self.UC_choice_no.config(background = "#292C4D",foreground="#ff8080")
		self.UC_choice_no.pack(side="left")

		NC_frame = tk.Frame(self.master)
		NC_frame.config(background = "#292C4D")
		NC_frame.pack()
		self.NC_label = tk.Label(NC_frame, text = "Number")
		self.NC_label.config(background = "#292C4D", foreground="#ff8080")
		self.NC_label.pack(side="left", padx=20, pady=5)

		NC_Radio_frame = tk.Frame(NC_frame)
		NC_Radio_frame.config(background = "#292C4D")
		NC_Radio_frame.pack(side="left")
		self.NC_choice_yes = tk.Radiobutton(NC_Radio_frame, text = "Yes", variable = self.NC_radio_val, value = True)
		self.NC_choice_yes.config(background = "#292C4D",foreground="#ff8080")
		self.NC_choice_yes.pack(side="left")
		self.NC_choice_no = tk.Radiobutton(NC_Radio_frame, text = "No", variable = self.NC_radio_val, value = False)
		self.NC_choice_no.config(background = "#292C4D",foreground="#ff8080")
		self.NC_choice_no.pack(side="left")

		self.button = tk.Button(self.master, text="Generate", command=self.generate)
		self.button.pack(pady=25)

		result_frame = tk.Frame(self.master)
		result_frame.pack()
		result_frame.config(background = "#292C4D")
		self.result = tk.Label(result_frame)
		self.result.config(background = "#292C4D", foreground="#ff8080", font=fontStyle2)
		self.result.pack(side="left")
		self.clipboard = tk.Button(result_frame, text="Copy", command=self.CopyToClipboard)
		self.clipboard.pack(side="right")


	def start(self):
		self.master.mainloop()

	def generate(self, event=None):
		rand = random.SystemRandom()
		try:
			input_entry = self.input_val.get()
		except tk.TclError:
			self.result['text'] = "Invalid input value"
			tk.messagebox.showerror(title="Invalid input!", message="Please type an integer")
		else:
			UC = string.ascii_uppercase if self.UC_radio_val.get() else ""
			SC = string.punctuation if self.SC_radio_val.get() else ""
			NC = string.digits if self.NC_radio_val.get() else ""
			alphabet = string.ascii_lowercase + UC + NC + SC
			password = str().join(rand.choice(alphabet) for _ in range(input_entry))
			self.result['text'] = password

	def CopyToClipboard(self):
		new_password = self.result['text']
		root.clipboard_clear()
		root.clipboard_append(new_password)

if __name__ == "__main__":
	root = tk.Tk()
	root.title("Password Generator")
	root.config(background = "#292C4D")
	root.geometry("500x300")
	root.minsize(width=550, height=400)
	root.resizable(width=False, height=False)
	app = App(root)
	app.start()
