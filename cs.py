from tkinter import*
import tkinter.messagebox
#import stddatabase

class Student:
    def __init__(self,root):
     self.root = root
     self.root.title("CS-Student-Management-Systems")
     self.root.geometry("1350x7500+0+0")
     self.root.config(bg="cadet blue")
     
     if __name=='__main__':
      root = Tk()
      application = Student(root)
      root.mainloop()
        
