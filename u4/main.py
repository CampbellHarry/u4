import tkinter as tk 

root =  tk.Tk() 
root.title('Assignment 2') 

window_width = 1000 
window_height = 700 

root.resizable(False, False)

screen_width = root.winfo_screenwidth() 
screen_height = root.winfo_screenheight()  

center_x = int(screen_width/2 - window_width / 2) 
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}') 

# Function to be called when button 1 is clicked
def adduser_clicked():
    print("Button 1 clicked")

# Function to be called when button 2 is clicked
def addteams_clicked():
    print("Button 2 clicked")

# Create Buttons
adduser = tk.Button(root, text="Add User", command=adduser_clicked)
addteams = tk.Button(root, text="Add Team", command=addteams_clicked)

# Place Buttons
adduser.place(relx=0.5, rely=0.5, anchor="center")
addteams.place(relx=0.5, rely=0.7, anchor="center")

# take edit out buttons
adduser.config(height=5, width=90)
addteams.config(height=5, width=90)


# Load Logo
logo_image = tk.PhotoImage(file="")

# Create Label to Display Logo
logo_label = tk.Label(root, image=logo_image)
logo_label.place(relx=0.5, rely=0.2, anchor="center")

root.mainloop() 
