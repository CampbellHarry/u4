import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 45)

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.iconphoto(True, tk.PhotoImage(file='logo (2) (1).png')) 
        self.title('College E-Sports')

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page1, Page2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self["bg"] = "black"
        
        # Load the image
        photo = tk.PhotoImage(file= "logo (2) (1).png")
        
        # Subsample the image
        # Subsample the image
        subsampled_image = photo.subsample(25)
        # Create the button with the subsampled image
        style =ttk.Style()
        style.theme_use("clam")
       

        style.configure("black.TButton",  background="#000", )
        button = ttk.Button(
            self, 
            image=subsampled_image, 
            command=lambda: controller.show_frame(StartPage ),
            style="black.TButton" 
            )
     
        button.photo = subsampled_image
        button.grid(row=0, column=0)
        

        label = ttk.Label(self, text="Welcome to College E-Sports", font=("Helvetica", 16), background='black', foreground='white')
        label.grid(row=0, column=1, padx=10, pady=10)
        button1 = ttk.Button(self, text="Add Player", command=lambda: controller.show_frame(Page1))
        button1.grid(row=1, column=0, padx=0, pady=20)

        button2 = ttk.Button(self, text="Add Team", command=lambda: controller.show_frame(Page2))
        button2.grid(row=1, column=1, padx=0, pady=20)

        button1 = ttk.Button(self, text="Add Player", command=lambda: controller.show_frame(Page1))
        button1.grid(row=1, column=0, padx=0, pady=20)

        button2 = ttk.Button(self, text="Add Team", command=lambda: controller.show_frame(Page2))
        button2.grid(row=1, column=1, padx=0, pady=20)

class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Page 1", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="StartPage", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Page 2", command=lambda: controller.show_frame(Page2))
        button2.grid(row=2, column=1, padx=10, pady=10)

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Page 1", command=lambda: controller.show_frame(Page1))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Startpage", command=lambda: controller.show_frame(StartPage))
        button2.grid(row=2, column=1, padx=10, pady=10)

app = tkinterApp()
app.mainloop()
