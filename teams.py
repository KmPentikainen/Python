from tkinter import *
from os import walk
import glob

teamlist = [
  ['Mithy', 'Support', 'Origen', 'Spain'],
  ['Caps', 'Mid',  'G2 Esports', 'Denmark'],
  ['Rekkles', 'ADC',  'Fnatic', 'Sweden'],
  ['Doublelift', 'ADC', 'Team Liquid', 'United States'],
  ['Bjergsen', 'Mid',  'TSM', 'Denmark'],
  ['Faker', 'Mid', 'SKT T1', 'South Korea'],
  ['Aphromoo', 'Support',  '100 Thieves', 'United States'],
  ['xPeke', 'Mid',    'Retired', 'Spain']
]


def whichSelected():
	print ("At %s of %s of %s of %s" % (nameVar, roleVar, teamVar, countryVar))
	return int(select.curselection()[0])    

def addbtn():
	teamlist.append ([nameVar.get(), roleVar.get(), teamVar.get(), countryVar.get()])
	setSelect ()


def updatebtn():
	teamlist[whichSelected()] = [nameVar.get(), roleVar.get(), teamVar.get(), countryVar.get()]
	setSelect()
	
def deletebtn():
	del teamlist[whichSelected()]
	setSelect()

def loadbtn():
	name, role, team, country = teamlist[whichSelected()]
	nameVar.set(name)
	teamVar.set(team)
	countryVar.set(country)
	roleVar.set(role)

def makeWindow():
	global nameVar, roleVar, teamVar, countryVar, select
	win = Tk()
	frame1 = Frame(win)
	frame1.pack()

	Label(frame1, text="Name").grid(row=0, column=0, sticky=W)
	nameVar = StringVar()
	name = Entry(frame1, textvariable = nameVar)
	name.grid(row=0, column=1, sticky=W)

	Label(frame1, text="Role").grid(row=1, column=0, sticky=W)
	roleVar = StringVar()
	role = Entry(frame1, textvariable = roleVar)
	role.grid(row=1, column=1, sticky=W)

	Label(frame1, text="Team").grid(row=2, column=0, sticky=W)
	teamVar = StringVar()
	team = Entry(frame1, textvariable = teamVar)
	team.grid(row=2, column=1, sticky=W)

	Label(frame1, text="Country").grid(row=3, column=0, sticky=W)
	countryVar =StringVar()
	country = Entry(frame1,textvariable = countryVar)
	country.grid(row=3, column=1, sticky=W)


	frame2 = Frame(win)
	frame2.pack()
	b1 = Button(frame2, text="Add", fg="red", command=addbtn)
	b1.pack(side=LEFT)

	b2 = Button(frame2, text="Update", command=updatebtn)
	b2.pack(side=LEFT)

	b3 = Button(frame2, text="Delete", command=deletebtn)
	b3.pack(side=LEFT)

	b4 = Button(frame2, text="Load", command=loadbtn)
	b4.pack(side=LEFT)

	frame3 = Frame(win)
	frame3.pack()
	scroll = Scrollbar(frame3, orient=VERTICAL)
	select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
	scroll.config(command=select.yview)
	scroll.pack(side=RIGHT, fill=Y)
	select.pack(side=LEFT, fill=BOTH, expand=1)
	return win

def setSelect():
	teamlist.sort()
	select.delete(0,END)
	for name, role, team, country in teamlist:
		select.insert(END, name)

win = makeWindow()
setSelect()
mainloop()