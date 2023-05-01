from tkinter import Canvas, Tk, Button, Entry, Label, PhotoImage, messagebox
import random
from gui import Interfaz
import database as db

BLANCO = "#FFFFFF"
NEGRO = "#000000"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range (random.randint(8,10))]
    password_symbols = [random.choice(symbols) for _ in range (random.randint(2,4))]
    password_numbers = [random.choice(numbers) for _ in range (random.randint(2,4))]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)
    generated_pwd = "".join(password_list)
    return generated_pwd


app = Tk()
app.config(bg=BLANCO, pady=50, padx=130)
app.minsize(680,580)
app.title("Account Manager")
interfaz = Interfaz(app)
interfaz.frame_login()


app.mainloop()




