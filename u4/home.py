# main menu code - Hours of hell spent on this 1.1 
import tkinter as tk
from tkinter import ttk


def adduser_clicked():
    print("Add a user clicked taking to page to add a user")

def addteams_clicked():
    print("add teams clicked taking to page to add teams")

def leaderboard_clicked():
    print("leaderboard clicked taking to page to show leaderboard")

def event_clicked():
    print("events clicked taking to page to show events")

# Create the main window
root = tk.Tk()
root.title('College E-Sports')
image = tk.PhotoImage(file="logo (2) (1).png")
root.iconphoto(False, image)
window_width = 1000
root["bg"] = "black"
window_height = 700
root.geometry(f'{window_width}x{window_height}+{root.winfo_screenwidth() // 2 - window_width // 2}+{root.winfo_screenheight() // 2 - window_height // 2}')
root.resizable(False, False)
style = ttk.Style()
style.configure("main.TButton", font=("Helvetica", 12))

# Create the top frame
label = ttk.Label(root, text="Welcome to HCollege E-Sports", font=("Helvetica", 16), background='black', foreground='white')
label.grid(row=0, column=0, columnspan=1, padx=10, pady=10)

# Resize the image to 100x100 pixels
image = image.subsample(25) 
label.img = image 
label.config(image=image, compound=tk.LEFT)

# Add an empty row for top margin
ttk.Label(root, background='black').grid(row=1)

# Configure the frame style to have a black background
style.configure("Black.TFrame", background="black")

# Create button frames
button_frame = ttk.Frame(root, style="Black.TFrame")
button_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=(5, 10))

# Configure button style
style.configure("main.TButton", font=("Helvetica", 12), foreground="black", borderwidth=0)

# Add user button
adduser_button = ttk.Button(button_frame, text="Add Player", command=adduser_clicked, style="main.TButton")
adduser_button.grid(row=0, column=0, padx=40, pady=60, sticky=tk.W, ipadx=60, ipady=20)

# Add teams button
addteams_button = ttk.Button(button_frame, text="Add Teams", command=addteams_clicked, style="main.TButton")
addteams_button.grid(row=0, column=1, padx=40, pady=60, sticky=tk.W, ipadx=60, ipady=20)

# Add leaderboard button
leaderboard_button = ttk.Button(button_frame, text="Leaderboard", command=leaderboard_clicked, style="main.TButton")
leaderboard_button.grid(row=1, column=0, padx=(0), pady=10, ipadx=60, ipady=20)

# Add events button
events_button = ttk.Button(button_frame, text="Events", command=event_clicked, style="main.TButton")
events_button.grid(row=1, column=1, padx=(0), pady=10, ipadx=60, ipady=20)

# Add an empty row for bottom margin
ttk.Label(root, background='black').grid(row=3)

# logout button
style.configure("main.Red.TButton", background="black", bg="blue", foreground="red", font=("Helvetica", 12))

logout_button = ttk.Button(root, text="Logout", command=root.quit, style="main.Red.TButton",)
logout_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10, ipadx=40, ipady=10)
# end of buttons

# Center the button frame within the window
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()

# end of main menu code