from tkinter import Frame,Label, Button, Entry, PhotoImage

BLANCO = "#FFFFFF"
NEGRO = "#000000"

class Interfaz():
    def __init__(self, root) -> None:
        self.root = root
        self.frame = self.create_frame()

    def create_frame(self):
        frame = Frame(self.root,  bg=BLANCO, width=600, height=500)
        frame.place(x=20,y=30)
        return frame

    def removethis(self):
        self.frame.destroy()

    def frame_login(self):
        self.removethis()
        
        login_frame = self.create_frame()
        login_frame.config(pady=10)

        frame_image = Frame(login_frame, borderwidth=2, bg=NEGRO)
        frame_image.grid(column=1, row=0)
        frame_image.picture = PhotoImage(file="logo.png")
        frame_image.label = Label(frame_image, image=frame_image.picture, bg=NEGRO)
        frame_image.label.grid(column=1,row=1)

        label_account_manager = Label(login_frame,text="Account Manager", font=("Arial", 25))
        label_account_manager.grid(column=1 ,row=1)
        label_account_manager.config(bg=BLANCO)

        label_username = Label(login_frame,text="Username:")
        label_username.config(bg=BLANCO, pady=10)
        label_username.grid(column=0,row=2)
        entrada_usuario = Entry(login_frame,highlightthickness=2, width=30)
        entrada_usuario.grid(column=1, row=2)
        
        label_password =Label(login_frame,text="Password:")
        label_password.config(bg=BLANCO, pady=2)
        label_password.grid(column=0,row=3)
        entrada_password = Entry(login_frame,highlightthickness=2, width=30)
        entrada_password.grid(column=1, row=3)

        frame1=Frame(login_frame,width=300, height=100, bg=BLANCO, pady=10)
        frame1.grid(column=1,row=4)

        login_button = Button(frame1,text="Log In")
        login_button.config(padx=5, borderwidth=3)
        login_button.grid(column=1, row=5)
        
        o_label = Label(frame1, text="Or")
        o_label.config(bg=BLANCO)
        o_label.grid(column=1, row=6)

        create_account_button = Button(frame1,text="Create Account", command=self.create_account)
        create_account_button.config(padx=5, borderwidth=3)
        create_account_button.grid(column=1, row=7)
        

    def create_account(self):
        self.removethis()
        frame_account = self.create_frame()
        frame_account.config(pady=10,padx=10)

        frame_image = Frame(frame_account, borderwidth=2, bg=NEGRO)
        frame_image.grid(column=1, row=0)
        frame_image.picture = PhotoImage(file="logo.png")
        frame_image.label = Label(frame_image, image=frame_image.picture, bg=NEGRO)
        frame_image.label.grid(column=1,row=1)

        label_create_account = Label(frame_account, text="Create Account",bg=BLANCO, pady=5, font=("arial",25))
        label_create_account.grid(column=1, row=1)

        nombre_label = Label(frame_account,text="First Name", bg=BLANCO, pady=5)
        nombre_label.grid(column=0,row=2)
        nombre_entrada = Entry(frame_account, highlightthickness=1)
        nombre_entrada.grid(column=1,row=2)

        apellido_label = Label(frame_account,text="Last Name", bg=BLANCO, pady=5)
        apellido_label.grid(column=0,row=3)
        apellido_entrada = Entry(frame_account, highlightthickness=1)
        apellido_entrada.grid(column=1,row=3)

        username_label = Label(frame_account,text="Username", bg=BLANCO, pady=5)
        username_label.grid(column=0,row=4)
        username_entrada = Entry(frame_account, highlightthickness=1)
        username_entrada.grid(column=1,row=4)

        passw_label = Label(frame_account,text="Password", bg=BLANCO, pady=5)
        passw_label.grid(column=0,row=5)
        passw_entrada = Entry(frame_account, highlightthickness=1)
        passw_entrada.grid(column=1,row=5)

        boton_volver = Button(frame_account, text="Volver", command=self.frame_login)
        boton_volver.grid(column=0, row=6)

