# A program to simulate a 6 face dice rolling
# Import the random module to pick a random image face
# Import the tkinter module to create the graphical user interface

import random
import tkinter as tk
from PIL import Image, ImageTk
# An instance of tkinter window
root = tk.Tk()
# Defining the width of the window
root.geometry('550x550')
# Definig the title of the window
root.title("Spencer's Dice Rolling Simulator")
# To prevent the window from being resized
# root.resizable(0,0)

# A heading for the window
heading = tk.Label(root, text = "Rolling Dice Simulator", font = "Helvitica 10 bold", bg = 'black', fg = 'white').pack()
# Defining the frame to display the photo
frame = tk.Frame(root, width = 500, height = 500, bg = 'sky blue').place(anchor = 'center', relx = 0.5, rely = 0.5)

# A list variable to store the six die images
image_list = ['die 1.png', 'die 2.png', 'die 3.png', 'die 4.png', 'die 5.png', 'die 6.png']

# A random image seletor
random_face = ImageTk.PhotoImage(Image.open(random.choice(image_list)))

# A label widget to display the images
image_label = tk.Label(frame, image = random_face)
#image_label.image = random_face
# for the image to always remain at the center even if resized
image_label.pack( expand = True)

# A function to roll the dice
def roll_dice():
    random_face = ImageTk.PhotoImage(Image.open(random.choice(image_list)))
    image_label.configure(image = random_face)
    image_label.image = random_face

play_button = tk.Button(root, text = 'Roll the Die', font = 'Arial 10', bg = 'green', fg = 'white', command = roll_dice).pack( expand = True)

exit_button = tk.Button(root, text = 'EXIT', font = 'Arial 10', bg = 'red', fg = 'white', command = root.destroy).pack( expand = True)

# To run the window
root.mainloop()
