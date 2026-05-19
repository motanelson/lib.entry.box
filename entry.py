import tkinter as tk

class myapp:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("hello world.......")
        self.root.configure(background="black")
        self.entry1=tk.Entry(background="black",foreground="white")
        self.entry1.pack(padx=10,pady=10)







root=tk.Tk()
apps=myapp(root)
root.mainloop()
