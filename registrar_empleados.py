import tkinter as tk
from tkinter import messagebox
import bcrypt
from connection import Connection
from sqlite3 import IntegrityError

# Clase que define la ventana de registro de trabajadores
class ViewRegistrarTrabajador(tk.Toplevel):
    
    #Constructor, recibe como parámetro la ventana padre, es decir la ventana desde donde se llama
    #y se definen los elementos que tendrá la ventana
    def __init__(self, parent):
        super().__init__(parent)
        # Crear la ventana
        self.title("Registro de Trabajador")
        self.geometry("700x600")  # Cambia el tamaño de la ventana (ancho x alto)

        # Agregar espacio horizontal entre los elementos
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.grid(row=0, column=0)

        #Titulo
        self.label_title = tk.Label(self, text="Registro de Trabajador", font=("Arial", 20))  # Cambia el tamaño de la letra
        self.label_title.grid(row=1, column=0, columnspan=3, padx=20)

        # Agregar espacio horizontal entre los elementos
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.grid(row=2, column=0)

        # Crear etiqueta y campo de entrada para el nombre
        self.label_nombre = tk.Label(self, text="Nombre:", font=("Arial", 14))  # Cambia el tamaño de la letra
        self.label_nombre.grid(row=3, column=0, sticky="w", padx=20)
        self.entry_nombre = tk.Entry(self, font=("Arial", 12))  # Cambia el tamaño de la letra
        self.entry_nombre.grid(row=3, column=1, padx=5, pady=5)

        # Agregar espacio horizontal entre los elementos
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.grid(row=4, column=0)

        # Crear etiqueta y campo de entrada para el Apellido Paterno
        self.label_ap_paterno = tk.Label(self, text="Apellido paterno:", font=("Arial", 14))  # Cambia el tamaño de la letra
        self.label_ap_paterno.grid(row=5, column=0, sticky="w", padx=20)
        self.entry_ap_paterno = tk.Entry(self, font=("Arial", 12))  # Cambia el tamaño de la letra
        self.entry_ap_paterno.grid(row=5, column=1, padx=5, pady=5)

        # Agregar espacio horizontal entre los elementos
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.grid(row=6, column=0)

        # Crear etiqueta y campo de entrada para el Apellido Materno
        self.label_ap_materno = tk.Label(self, text="Apellido materno:", font=("Arial", 14))  # Cambia el tamaño de la letra
        self.label_ap_materno.grid(row=7, column=0, sticky="w", padx=20)
        self.entry_ap_materno = tk.Entry(self, font=("Arial", 12))  # Cambia el tamaño de la letra
        self.entry_ap_materno.grid(row=7, column=1, padx=5, pady=5)

        # Agregar espacio horizontal entre los elementos
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.grid(row=8, column=0)

        # Crear etiqueta y campo de entrada para el username
        self.label_username = tk.Label(self, text="Nombre de usuario:", font=("Arial", 14))  # Cambia el tamaño de la letra
        self.label_username.grid(row=9, column=0, sticky="w", padx=20)
        self.entry_username = tk.Entry(self, font=("Arial", 12))  # Cambia el tamaño de la letra
        self.entry_username.grid(row=9, column=1, padx=5, pady=5)

        # Agregar espacio horizontal entre los elementos
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.grid(row=10, column=0)

        self.label_password = tk.Label(self, text="Contraseña:", font=("Arial", 14))  # Cambia el tamaño de la letra
        self.label_password.grid(row=11, column=0, sticky="w", padx=20)
        self.entry_password = tk.Entry(self, font=("Arial", 12), show="*")  # Cambia el tamaño de la letra
        self.entry_password.grid(row=11, column=1, padx=5, pady=5)

        self.show_password_button = tk.Button(self, text="Mostrar", command=self.toggle_password_visibility)
        self.show_password_button.grid(row=11, column=2, padx=5, pady=5)

        # Agregar espacio horizontal entre los elementos
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.grid(row=12, column=0)

        # Crear etiqueta y lista desplegable para el horario
        self.label_horario = tk.Label(self, text="Horario:", font=("Arial", 14))  # Cambia el tamaño de la letra
        self.label_horario.grid(row=13, column=0, sticky="w", padx=20)
        self.combo_horario = tk.StringVar()
        self.combo_horario.set("Lunes - Sábado, Matutino (8:30am-3:00pm)")  # Valor predeterminado
        self.combo_horario_menu = tk.OptionMenu(self, self.combo_horario, "Lunes - Sábado, Matutino (8:30am-3:00pm)", "Lunes - Sábado, Vespertino (2:30pm-10:00pm)")
        self.combo_horario_menu.config(font=("Arial", 12))  # Cambia el tamaño de la letra
        self.combo_horario_menu.grid(row=13, column=1, padx=5, pady=5)

        # Agregar espacio horizontal entre los elementos
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.grid(row=14, column=0)

        # Crear botón de registro
        self.btn_registrar = tk.Button(self, text="Registrar", command=self.registrar_trabajador, font=("Arial", 14))  # Cambia el tamaño de la letra
        self.btn_registrar.grid(row=15, column=0, columnspan=3, pady=10)
    

    def registrar_trabajador(self):
        nombre = self.entry_nombre.get()
        horario = self.combo_horario.get()
        ap_pat = self.entry_ap_paterno.get()
        ap_mat = self.entry_ap_materno.get()
        username = self.entry_username.get()
        password = self.entry_password.get()

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
        elif password == "":
            messagebox.showerror("Error", "Debes ingresar una contraseña.")
        else:
            # Aquí puedes realizar cualquier operación adicional con los datos del trabajador
            #Registrar en la base de datos
            password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            conn = Connection("./BaseDeDatos/ElUltimoJardin.db")
            con = conn.connect()
            
            if (con):
                cursor = conn.conn.cursor()
                
                try:
                    # Ejecutar una operación que puede generar una excepción de unicidad
                    cursor.execute("INSERT INTO empleados (nombre, apellido_paterno, apellido_materno, username, password, horario) VALUES (?, ?, ?, ?, ?, ?)", (nombre, ap_pat, ap_mat, username, password_hash, horario))
                    conn.conn.commit()
                    messagebox.showinfo("Registro exitoso", f"Trabajador {nombre}, y nombre de usuario {username} registrado con horario {horario}.")
                except IntegrityError:
                    # Manejar la excepción de unicidad
                    messagebox.showerror("Error", "El nombre de usuario ya existe")
                except Exception as e:
                    # Manejar cualquier otra excepción
                    messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")
                    conn.conn.rollback()
                finally:
                    # Cerrar la conexión a la base de datos
                    conn.conn.close()
            else:
                messagebox.showerror("Error", "Comunicación con la base de datos fallida.")
                
            
           
            
    def toggle_password_visibility(self):
        current_show_state = self.entry_password.cget("show")
        if current_show_state == "":
            self.entry_password.configure(show="*")
            self.show_password_button.configure(text="Mostrar")
        else:
            self.entry_password.configure(show="")
            self.show_password_button.configure(text="Ocultar")

# if __name__ == "__main__":
#     registrarVtn = ViewRegistrarTrabajador(None)
#     registrarVtn.mainloop()
    
    
    # Verificar si una contraseña coincide con la versión encriptada almacenada en la base de datos
    # def validatePassword(self, username, password):
    #     cursor = self.conn.cursor()
    #     cursor.execute("SELECT password FROM empleados WHERE username = ?", (username,))
    #     row = cursor.fetchone()
    #     if row:
    #         return bcrypt.checkpw(password.encode("utf-8"), row[0])
    #     else:
    #         return False