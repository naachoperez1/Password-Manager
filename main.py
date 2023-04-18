from tkinter import Canvas, Tk, Button, Entry, Label, PhotoImage, messagebox
import random

# ---------------------------- GLOBALS ------------------------------- #
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
    passwor = "".join(password_list)

    entrada_password.delete(0, 'end')
    entrada_password.insert(0, passwor)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    pagina = entrada_website.get()
    pagina_mayuscula = pagina.upper()
    usuario = entrada_usuario.get()
    usuario_mayuscula = usuario.upper()
    passw = entrada_password.get()
    texto = {pagina_mayuscula:{
            "Usuario":usuario_mayuscula,
            "Password":passw
    }
    }

    if len(pagina) == 0 or len(passw) == 0 or len (usuario) ==0:
        messagebox.showwarning("Error", "Por favor, completa todos los campos")
    else:
        is_ok = messagebox.askyesno(title="Confirme datos", message=f"Pagina : {pagina.title()}\nUsuario : {usuario}\nContraseña : {passw}\nDesea guardar?")
        if is_ok:
            try:
                # Abrimos el archivo.json en modo lectura.
                with open("contraseñas.json","r") as data_file:
                    # Leemos los datos viejos y lo guardamos en la variable data.
                    data = json.load(data_file)
                    # Actualizamos la variable data con el metodo update(datos nuevos).
                    data.update(texto)

            # Si no hay nada escrito en el archivo.json, no hay nada que guardar en la variable data y eso genera un JSONDecodeError.
            except json.JSONDecodeError:
                print("JSONDecodeError")
                with open("contraseñas.json", "w") as data_file:
                    json.dump(texto, data_file, indent=4)

            # Si no existe el archivo.json, lo creamos y escribimos los datos.
            except FileNotFoundError:
                print("FileNotFoundError")
                with open("contraseñas.json", "w") as data_file:
                    json.dump(texto, data_file, indent=4)
            else:
                # Abrimos el archivo.json en modo escritura.
                with open ("contraseñas.json", "w") as data_file:
                    # Sobreescribimos el archivo con la variable data. (Datos viejos + datos nuevos).
                    json.dump(data, data_file, indent=4)

            finally:
                messagebox.showinfo("Gestor de contraseñas", "La contraseña ha sido guardada extiosamente")
                entrada_website.delete(0,'end')
                entrada_password.delete(0,'end')


# ---------------------------- GET PASSWORD ------------------------------- #
def get_password(): # Busca los datos de la pagina ingresada(usuario y contraseña), y los muestra en un messagebox
    try:
        pagina = entrada_website.get()
        pagina_mayuscula = pagina.upper()
        with open("contraseñas.json", "r") as data_file:
            datos_pagina = json.load(data_file)[pagina_mayuscula]
    except KeyError:
        messagebox.showinfo("Error", "Los datos de la pagina que desea buscar no se encuentra.\nAsegurese de ingresar el nombre de la web correctamente.")
    else:
        usuario = datos_pagina["Usuario"]
        password = datos_pagina["Password"]
        messagebox.showinfo(pagina.title(),f"Usuario : {usuario.lower()}\nContraseña : {password}")

# ---------------------------- UI SETUP ------------------------------- #
#   WINDOW  #
window = Tk()
window.config(bg=BLANCO, pady=50, padx=50)
window.title("Pasword Manager")
window.minsize(400, 400)

#   CANVAS  #
canvas = Canvas(width=200, height=200, bg=NEGRO, highlightthickness=5)
locker_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=locker_img)
canvas.grid(column=1, row=0)

#   LABELS  #
website = Label(text="Website:", font=("Arial", 10))
website.config(bg=BLANCO)
website.grid(column=0, row=1)

email = Label(text="Email:", font=("Arial", 10))
email.config(bg=BLANCO)
email.grid(column=0,row=2)

password = Label(text="Password:", font=("Arial", 10))
password.config(bg=BLANCO)
password.grid(column=0, row=3)

#   Entrys  #
entrada_website = Entry(width=33)
entrada_website.focus()
entrada_website.grid(row=1, column=1)
entrada_website.config(borderwidth=2)


entrada_usuario = Entry(width=33)
entrada_usuario.insert(0)
entrada_usuario.grid(row=2, column=1)
entrada_usuario.config(borderwidth=2)

entrada_password = Entry(width=33)
entrada_password.grid(row=3, column=1)
entrada_password.config(borderwidth=2)

#   BUTTONS  #
generate_button = Button(text="Generate Password", width=18, command=generate_password)
generate_button.grid(row=3, column=2)
generate_button.config(borderwidth=2)

get_button = Button(text="Search", width=18, command=get_password)
get_button.grid(row=1, column=2)
get_button.config(borderwidth=2)

add_button = Button(text="Add Password", width=48, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
