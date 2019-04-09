
import sys
import os
import tkinter as tk

root = tk.Tk()



class submit(tk.Frame):
	pass

class view_finance(tk.Frame):

	def __init__(self, master):
		tk.Frame.__init__(self)               
		#self.myfinance = myfinance
		master.title("Spending tracker")





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

		viewbutton = tk.Button(master, text='View Finance', command=view_finance)
		viewbutton.grid(row=9, column=1)

root.geometry("500x580+500+500")
app = Window(root)
root.mainloop()