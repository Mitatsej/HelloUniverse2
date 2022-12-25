#POOP OOP-IN PYTHON ----> and other class
#firstclass
'''
from car import Car
car1 = Car("BMV","mONEY",2002,"BLU")
print(car1.model)
print(car1.make)
print(car1.color)
print(car1.year)

car1.drive()
car1.stop()


##second class
class Car:

    def __init__(self,make,model,year,color):
        self.model = model #instance variable
      #  self.make = make  #instance variable
      #  self.year = year   #instance variable
      # self.color = color #instance variable

    def drive(self):
        print("The car is moving")

    def stop(self):
        print("The car is stoping")


#inheritance --trashegimia
class Animal :
    alive = True

    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")
class Rabbit(Animal): #mujn me perdor gjdo sen te klases animal
    pass
class Fish(Animal):
    pass
class Hawk(Animal):
    pass

hawk = Hawk()
fish = Fish() #i deklarojm objektett
rabbit = Rabbit()
hawk.eat()'''


#krijimi i GUI
'''
from tkinter import *
window = Tk() #instantoj një shembull të një dritareje
window.geometry("420x420")
window.title("Mit Baba first GUI")
window.config(background="#5cfcff")

window.mainloop() #vendos dritaren në ekranin e kompjuterit

#krijimi i label

from tkinter import *
window = Tk()
label = Label(window,
              text="EIIII SHOKI",
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              )
label.pack()

window.mainloop()'''

#Mini app with some function
'''
from tkinter import *

def submit():
    username = entry.get()
    print("Hello " + username)

def delete():
    entry.delete(0,END)
def backspace():
    entry.delete(len(entry.get())-1,END)
window = Tk()

entry = Entry(window,
              font=("Arial",50),
              fg="00FF00",
              bg="black")
entry.pack(side=LEFT)

submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="delete",command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text="backspace",command=backspace)
backspace_button.pack(side=RIGHT)


window.mainloop()'''

#MENU BAR
'''
from tkinter import *

def openFile():
    print("File is been opened")

def saveFile():
    print("File is been saved")
window = Tk()
menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)

window.mainloop()'''

