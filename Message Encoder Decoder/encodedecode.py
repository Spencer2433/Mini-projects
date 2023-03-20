# a program to encode and decode a message

# import tkinter for graphical user interface
# import base64 to encode binary data to ASCII characters and decode that ASCII characters back to binary data
import tkinter as tk
import base64

# create an application window called root
root = tk.Tk()
# set the size of the application window
root.geometry('500x300')
# prevent the window from being resized
root.resizable(0,0)
# set the title of the window
root.title("Spencer's Message Encoder and Decoder")
# Set background colour
root.configure(bg= "sky blue")

# Labels for the window
top_label = tk.Label(root, text = "Spencer's message encode and decode", font = 'helvitica 12', bg = 'purple', fg = 'white' ).pack()
bottom_label = tk.Label(root, text = 'atanima', font = 'calibri 12', bg = 'grey', fg = 'red').pack(side =tk.BOTTOM)

# Variable to store the message to encode
text = tk.StringVar()
# Variable to store private key used to encode decode
private_key = tk.StringVar()
# Variable to select whether to eccode or decode
mode = tk.StringVar()
# Variable to store the result
result = tk.StringVar() 

# Function to encode
def encode(key, message):
    # An empty list
    enc = []

    # We run the loop till the length of the message
    for i in range(len(message)):
        # % of len(key) gives the remainder of division between i and len(key)
        # The remainder is used as an index of key
        # The value of that key, at that index is stored in key_c
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c))% 256))
    return base64.urlsafe_b64encode(" ".join(enc).encode()).decode()

# Function to decode
def decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return " ".join(dec)

# Function to set mode
def Mode():
    if (mode.get() == 'e'):
        result.set(encode(private_key.get(), text.get()))
    elif(mode.get() == 'd'):
        result.set(decode(private_key.get(), text.get()))
    else:
        result.set('Invalid Mode')

# Function to exit window
def Exit():
    root.destroy()

# Function to reset window
def Reset():
    text.set('')
    private_key.set('')
    mode.set('')
    result.set('')

tk.Label(root, font= 'arial 12 bold', text='MESSAGE').place(x= 60,y=60)
tk.Entry(root, font = 'arial 10', textvariable = text, bg = 'ghost white').place(x=290, y = 60)

tk.Label(root, font = 'arial 12 bold', text ='KEY').place(x=60, y = 90)
tk.Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)

tk.Label(root, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)').place(x=60, y = 120)
tk.Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)
tk.Entry(root, font = 'arial 10 bold', textvariable = result, bg ='ghost white').place(x=290, y = 150)

tk.Button(root, font = 'arial 10 bold', text = 'RESULT'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=60, y = 150)

tk.Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=80, y = 190)

tk.Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=180, y = 190)

root.mainloop()

root.mainloop()