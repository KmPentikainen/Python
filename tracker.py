#from tkinter import *
import sys
import os
#import calculator2

import tkinter as tk

#from tkinter.ttk import Frame, Label, Style



class Window(tk.Frame):

	def __init__(self, master=None):
		tk.Frame.__init__(self, master)               
		self.master = master
		master.title("Spending tracker")

		years = {'2019', '2020', '2021'}

		popYears = tk.OptionMenu(master, *years)
		tk.Label(master, text="Year: ").grid(row=1, column=0)
		popYears.grid(row=1, column=1)

		months = {'Janruary', 'February', 'March', 'April', 'May', 'June', 'July'}

		popMonths = tk.OptionMenu(master, *months)
		tk.Label(master, text="Month: ").grid(row=2, column=0)
		popMonths.grid(row=2, column=1)

		tk.Label(master, text="Salary: ").grid(row=5, column=0)
		salaryVar = tk.StringVar()
		salary = tk.Entry(master, textvariable = salaryVar)
		salary.grid(row=5, column=1)

		tk.Label(master, text="Bills total: ").grid(row=6, column=0)
		billsVar = tk.StringVar()
		bills = tk.Entry(master, textvariable = billsVar)
		bills.grid(row=6, column=1)

		tk.Label(master, text="Monthly savings: ").grid(row=7, column=0)
		monsavVar = tk.StringVar()
		monsav = tk.Entry(master, textvariable = monsavVar)
		monsav.grid(row=7, column=1)

		submitbutton = tk.Button(master, text='Submit', command=submit)
		submitbutton.grid(row=8, column=1)

class submit():
	pass


		#calculatorbtn = tk.Button(master, text='Calculator', command=callcalculator)
		#calculatorbtn.grid(row=7, column=1)



#class callcalculator(tk.Frame):
#	def callcalclulator():
#		os.system('calculator2.py')

	






	

		


root = tk.Tk()
root.geometry("500x580+500+500")
app = Window(root)
root.mainloop()