import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 45)

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.iconphoto(True, tk.PhotoImage(file='logo.png')) 
        self.title('College E-Sports')
        self.geometry("600x750")

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

    def create_element(self, page):
        # Get the text from the Text widget
        element_name = page.text_box.get("1.0", "end-1c")

        # Create a frame to contain the element details
        element_details_frame = tk.Frame(page.element_frame, bg="white")
        element_details_frame.pack(side="top", fill="x", padx=40, pady=10, ipady=5)

        # Label for the element name
        name_label = tk.Label(element_details_frame, text=f"{element_name}", bg="white")
        name_label.pack(side="top", fill="x")

        # Button to add players
        add_player_button = tk.Button(element_details_frame, text="Add Player", bg="#000", fg="#fff", command=lambda: self.add_player(element_details_frame))
        add_player_button.pack(side="top", pady=5)

        # Increment the element counter
        page.element_counter += 1

    def add_player(self, parent):
        # Create a frame to contain player input
        player_frame = tk.Frame(parent, bg="white")
        player_frame.pack(side="top", fill="x", padx=10, pady=5, ipady=5)

        # Text box for player's name and total score
        player_name_entry = tk.Entry(player_frame, width=30)
        player_name_entry.pack(side="left", padx=(0, 10))
        player_score_entry = tk.Entry(player_frame, width=10)
        player_score_entry.pack(side="left", padx=(0, 10))

        # Button to append player information
        append_button = tk.Button(player_frame, text="Append", bg="#000", fg="#fff")
        append_button.pack(side="left")


class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self["bg"] = "black"
        self.photo = tk.PhotoImage(file='logo.png')
        self.photo = self.photo.subsample(20)
        self.image_label = ttk.Label(
            self,
            background= "#000",
            image = self.photo,
            padding = 5,
            foreground= "#fff",
            text = "Add player",
            compound = "left",
            font = ("Helvetica", 20)
        ) 
        self.image_label.pack()

        self.label_title = ttk.Label(
            self,
            text="Add a event",
            background="#000",
            foreground="#fff",
            padding="30",
            font = ("Helvetica", 13)
        )
        self.label_title.pack()
        
        self.text_box = tk.Text(self, height=2, width=50)
        self.text_box.pack()

        # Button
        button = tk.Button(self, text="Create new event", height=2, width=30, pady=10, padx=10, bg="#000", fg="#fff")
        button["command"] = lambda: controller.create_element(self)
        self.element_counter = 0
        button.pack(pady=10)

        # Frame to contain the elements
        self.element_frame = tk.Frame(self, bg="black")
        self.element_frame.pack()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self["bg"] = "black"
        self.photo = tk.PhotoImage(file='logo.png')
        self.photo = self.photo.subsample(20)
        self.image_label = ttk.Label(
            self,
            background= "#000",
            image = self.photo,
            padding = 5,
            foreground= "#fff",
            text = "College Esports",
            compound = "left",
            font = ("Helvetica", 20)
        ) 
        self.image_label.pack()

        self.event_button = ttk.Button(self, text="View Events")
        self.event_button["command"] = lambda: controller.show_frame(Page1)
        self.event_button.pack(fill = "both", expand="true", padx=150,ipady=20, pady=20)

        self.teams_button = ttk.Button(self, text="Add Teams")
        self.teams_button.pack(fill = "both", expand="true", padx=150, ipady=20, pady=20)

        self.add_button = ttk.Button(self, text="Add Players")
        self.add_button.pack(fill = "both", expand="true", padx=150, ipady=20, pady=20)

        self.run_button = ttk.Button(self, text="Run Tournaments")
        self.run_button.pack(fill = "both", expand="true", padx=150, ipady=20, pady=20)

        self.leader_button = ttk.Button(self, text="Leaderboard")
        self.leader_button.pack(fill = "both", expand="true", padx=150, ipady=20, pady=20)

class Page2(tk.Frame):
   def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self["bg"] = "black"
        
        # Load the image
        photo = tk.PhotoImage(file="logo.png")
        
        # Subsample the image
        subsampled_image = photo.subsample(25)
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("black.TButton", background="#000")

        button = ttk.Button(
            self, 
            image=subsampled_image, 
            command=lambda: controller.show_frame(StartPage),
            style="black.TButton" 
        )
        # buttons
        button.photo = subsampled_image
        button.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        label = ttk.Label(self, text="Add a Team", font=("Helvetica", 16), background='black', foreground='white')
        label.grid(row=0, column=1, padx=0, pady=10, sticky="w")

        # Configure grid to center all widgets to the screen
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
app = tkinterApp()
app.mainloop()