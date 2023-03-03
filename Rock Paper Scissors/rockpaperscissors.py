# A program to play rock, paper, scissors against the computer

# Import tkinter as a graphical user interface
# Import random to choose rock paper or scissors randomly 
import tkinter as tk
import random

# Create an application window called root
root = tk.Tk()
# Set it's size using .geometry() method to 400 by 400
root.geometry('500x300')
# Set that the size of the window cannot be adjusted
root.resizable(0,0)
# Configure the background color
root.configure(bg = 'seashell3')
# Choose a title for your application window
root.title(f"Spencer's--Rock, Paper, Sciccors")

# A title to appear at the top of the game window
game_label = tk.Label(root, text = "Rock Paper Scissors", width = 20, font = "Arial 20 bold", bg = 'seashell2')
game_label.pack(pady = 5)

# To display to the user what to input and take user input
user_input = tk.StringVar()
tk.Label(root, text = "Choose rock paper or scissors : ", font = 'Arial 15', bg = 'seashell2').place(x = 10, y = 50)
tk.Entry(root, width = 15, bg = 'white', font = 'Arial', textvariable = user_input, justify = 'center').place(x = 320, y = 55)


result = tk.StringVar()

def play():
    # For the computer choice we select a random choice from the choises list
    # This return the choice as a list hence we call it via [0]
    comp_choice = random.choices(['rock', 'paper', 'scissors'])[0]

    user_pick = user_input.get() # to access user_input which is outside our function
    if user_pick == comp_choice:
        result.set("The game is a tie!")

    elif user_pick == 'rock' and comp_choice == 'paper':
        result.set("You lost. Computer picked paper.")

    elif user_pick == 'rock' and comp_choice == 'scissors':
        result.set("You win. Computer picked scissors.")

    elif user_pick == 'paper' and comp_choice == 'scissors':
        result.set("You lost. Computer picked scissors.")

    elif user_pick == 'paper' and comp_choice == 'rock':
        result.set("You win. Computer picked rock.")

    elif user_pick == 'scissors' and comp_choice == 'rock':
        result.set("You lost. Computer picked rock.")

    elif user_pick == 'scissors' and comp_choice == 'paper':
        result.set("You win. Computer picked paper.")
    else:
        result.set("Invalid choice. Pick between rock paper and scissors")

# Function to reset once a round has been completed
def reset():
    user_input.set("")
    game_outcome.set("")
    result.set("")

# Function to exit the game
def exit():
    root.destroy()

play_button = tk.Button(root, text = "PLAY", width = 7, height = 1, padx = 5,bg = 'seashell2', font = 'Arial', command = play).place(x = 350, y = 100)

game_outcome = tk.StringVar()
tk.Entry(root, width = 50, font = 'Arial', textvariable = result).place( x = 5, y = 150)

reset_button = tk.Button(root, text = "RESET", width = 7, height = 1, padx = 5, bg = 'seashell2', font = 'Arial', command = reset).place(x = 100, y = 200)

exit_button = tk.Button(root, text = "EXIT", width = 5, height = 1, bg = 'seashell2', font = 'Arial', command = exit).place(x = 300, y = 200)

# Run the application window
root.mainloop()