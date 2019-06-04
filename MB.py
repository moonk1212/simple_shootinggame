from tkinter import *
import clsmain


class mb(Frame):

    
    def __init__(self, master=None):
                
        Frame.__init__(self, master)   
                
        self.master = master
        self.init_window()
        


    def init_window(self):
   
        self.master.title("Snow Fighter")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        startButton = Button(self, text="Start",command=clsmain)
        startButton.place(x=180,y=150)
        startButton.pack()
        lb=Label(text="Snow Fighter",width=50,height=3)       
        lb.pack()
        
        
    def client_exit(self):
        exit()

    
 
