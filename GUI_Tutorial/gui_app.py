#from tkinter, root = tk(), root.mainloop()  are basic layouts needed fro GUI
from tkinter import *

root = Tk()

#making invisible container that goes in mainroot.Works by default
topFrame = Frame(root)
#anytime you want anything displayed you have to pack it in. place it somewhere in main program or window
topFrame.pack()
bottomFrame =Frame(root)
bottomFrame.pack(side=BOTTOM)
#throw in parameter in bottom frame to put where it is
#name object button and the first parameter is what frame .
#Fg is set to equal to a color
#buttons1-3 will go in top rectangle and button 4 will go in bottom.
button1 = Button(topFrame, text= "Button 1", fg="red")# the text will be red not the button
button2 = Button(topFrame, text= "Button 2", fg="blue")
button3 = Button(topFrame, text= "Button 3", fg="purple")
button4 = Button(bottomFrame, text= "Button 4", fg="yellow")
#buttons placement
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side= LEFT)
button4.pack(side= BOTTOM)

root.mainloop()
