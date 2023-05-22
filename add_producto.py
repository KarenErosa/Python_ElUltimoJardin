import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class ViewRegistrarProducto(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_window = parent
        
        self.conn = sqlite3.connect('./BaseDeDatos/ElUltimoJardin.db')
        self.cursor = self.conn.cursor()
        
        self.title("Registrar Producto")
        self.geometry("500x400")
        
        self.categorias = {}
        
        self.crear_interfaz()
        
        return self
    
    def crear_interfaz(self):
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.pack()
        
        self.label_title = tk.Label(self, text="Registrar Producto", font=("Arial", 20))
        self.label_title.pack()
        
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.pack()
        
        nombre_label = tk.Label(self, text="Nombre:")
        nombre_label.pack()
        self.nombre_entry = tk.Entry(self, width=35)
        self.nombre_entry.pack()
        
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.pack()
        
        categoria_label = tk.Label(self, text="Categoría:")
        categoria_label.pack()
        
        self.categorias = dict(self.main_window.obtener_categorias())
        self.categoria_combo = ttk.Combobox(self, values=list(self.categorias.values()), state="readonly", width=35)
        self.categoria_combo.pack()
        
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.pack()
        
        precio_label = tk.Label(self, text="Precio:")
        precio_label.pack()
        self.precio_entry = tk.Entry(self, validate="key", width=35)
        self.precio_entry.config(validatecommand=(self.precio_entry.register(self.validar_precio), '%P'))
        self.precio_entry.pack()
        
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.pack()
        
        registrar_button = tk.Button(self, text="Registrar", command=self.registrar_producto)
        registrar_button.pack()
        
        
        self.mainloop()
    
    def registrar_producto(self):
        nombre = self.nombre_entry.get()
        precio = self.precio_entry.get()    
        categoria = self.categoria_combo.get()
        
        
        if nombre == "":
            messagebox.showerror("Error", "El nombre es obligatorio")
        elif precio == "":
            messagebox.showerror("Error", "El precio es obligatorio")
        elif categoria == "":
            messagebox.showerror("Error", "La categoría es obligatoria")
        else:
            try:
                categoria_id = list(self.categorias.keys())[list(self.categorias.values()).index(categoria)]
                self.cursor.execute("INSERT INTO productos (nombre, precio, categoria_id) VALUES (?, ?, ?)", (nombre, precio, categoria_id))
                self.conn.commit()
                messagebox.showinfo("Éxito", "Producto registrado correctamente")
                self.main_window.llenarProductos()
                self.destroy()
            except Exception as e:
                messagebox.showerror("Error", "Ocurrió un error al registrar el producto")
    
    
    def validar_precio(self, valor):
        try:
            float(valor)
            return True
        except ValueError:
            if valor == "":
                return True
            else:
                return False
