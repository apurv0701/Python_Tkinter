import sys
from tkinter import *
def main ():
    root = Tk()
    button = Button(master=root,activebackground = "blue",
                    text='hello',
                    command = quit_callback)
    button.pack()
    
    #root = Tk()
    button = Button(root,text='h',command = quit_callback)
    button.pack()
    root.mainloop()
   
def quit_callback():
    sys.exit(0)
    


main()
