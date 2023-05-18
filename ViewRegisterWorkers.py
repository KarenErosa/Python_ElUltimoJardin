import tkinter as tk
from tkinter import messagebox

# Clase que define la ventana de registro de trabajadores
class ViewRegistrarTrabajador(tk.Toplevel):
    
    #Constructor, recibe como parámetro la ventana padre, es decir la ventana desde donde se llama
    #y se definen los elementos que tendrá la ventana
    def __init__(self, parent):
        super().__init__(parent)
        # Crear la ventana
        self.title("Registro de Trabajador")
        self.geometry("450x570")  # Cambia el tamaño de la ventana (ancho x alto)

        # Agregar espacio horizontal entre los elementos
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.pack()

        #Titulo
        self.label_title = tk.Label(self, text="Registro de Trabajador", font=("Arial", 20))  # Cambia el tamaño de la letra
        self.label_title.pack()

        # Agregar espacio horizontal entre los elementos
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.pack()

        # Crear etiqueta y campo de entrada para el nombre
        self.label_nombre = tk.Label(self, text="Nombre:", font=("Arial", 14))  # Cambia el tamaño de la letra
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(self, font=("Arial", 12))  # Cambia el tamaño de la letra
        self.entry_nombre.pack()

        # Agregar espacio horizontal entre los elementos
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.pack()

        # Crear etiqueta y campo de entrada para el Apellido Paterno
        self.label_ap_paterno = tk.Label(self, text="Apellido paterno:", font=("Arial", 14))  # Cambia el tamaño de la letra
        self.label_ap_paterno.pack()
        self.entry_ap_paterno = tk.Entry(self, font=("Arial", 12))  # Cambia el tamaño de la letra
        self.entry_ap_paterno.pack()

        # Agregar espacio horizontal entre los elementos
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.pack()

        # Crear etiqueta y campo de entrada para el Apellido Materno
        self.label_ap_materno = tk.Label(self, text="Apelldio materno:", font=("Arial", 14))  # Cambia el tamaño de la letra
        self.label_ap_materno.pack()
        self.entry_ap_materno = tk.Entry(self, font=("Arial", 12))  # Cambia el tamaño de la letra
        self.entry_ap_materno.pack()

        # Agregar espacio horizontal entre los elementos
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.pack()

        # Crear etiqueta y campo de entrada para el username
        self.label_username = tk.Label(self, text="Nombre de usuario:", font=("Arial", 14))  # Cambia el tamaño de la letra
        self.label_username.pack()
        self.entry_username = tk.Entry(self, font=("Arial", 12))  # Cambia el tamaño de la letra
        self.entry_username.pack()

        # Agregar espacio horizontal entre los elementos
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.pack()

        # Crear etiqueta y lista desplegable para el horario
        self.label_horario = tk.Label(self, text="Horario:", font=("Arial", 14))  # Cambia el tamaño de la letra
        self.label_horario.pack()
        self.combo_horario = tk.StringVar()
        self.combo_horario.set("Matutino (8:30am-3:00pm)")  # Valor predeterminado
        self.combo_horario_menu = tk.OptionMenu(self, self.combo_horario, "Lunes - Sábado, Matutino (8:30am-3:00pm)", "Lunes - Sábado, Vespertino (2:30pm-10:00pm)")
        self.combo_horario_menu.config(font=("Arial", 12))  # Cambia el tamaño de la letra
        self.combo_horario_menu.pack()

        # Agregar espacio horizontal entre los elementos
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.pack()
        
        
        # Crear botón de registro
        self.btn_registrar = tk.Button(self, text="Registrar", command=self.registrar_trabajador, font=("Arial", 14))  # Cambia el tamaño de la letra
        self.btn_registrar.pack()
        

    def registrar_trabajador(self):
        nombre = self.entry_nombre.get()
        horario = self.combo_horario.get()
        ap_pat = self.entry_ap_paterno.get()
        ap_mat = self.entry_ap_materno.get()
        username = self.entry_username.get()

        if nombre == "":
            messagebox.showerror("Error", "Debes ingresar un nombre.")
        elif horario == "":
            messagebox.showerror("Error", "Debes seleccionar un horario.")
        elif ap_pat == "":
            messagebox.showerror("Error", "Debes ingresar un apellido paterno.")
        elif ap_mat == "":
            messagebox.showerror("Error", "Debes ingresar un apellido materno.")
        elif username == "":
            messagebox.showerror("Error", "Debes ingresar un nombre de usuario.")
        else:
            # Aquí puedes realizar cualquier operación adicional con los datos del trabajador
            #Registrar en la base de datos
            messagebox.showinfo("Registro exitoso", f"Trabajador {nombre}, y nombre de usuario {username} registrado con horario {horario}.")



# if __name__ == "__main__":
#     registrarVtn = ViewRegistrarTrabajador(None)
#     registrarVtn.mainloop()