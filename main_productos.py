import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from add_producto import ViewRegistrarProducto

class ViewProductos(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_window = parent
        
        self.conn = sqlite3.connect('./BaseDeDatos/ElUltimoJardin.db')
        self.cursor = self.conn.cursor()
        
        self.title("CRUD de Productos")
        self.geometry("500x400")
        
        self.productos = {}
        self.categorias = {}
        
        self.crear_interfaz()


    def obtener_categorias(self):
        self.cursor.execute("SELECT id, nombre FROM categorias")
        return self.cursor.fetchall()

    def obtener_productos(self):
        self.cursor.execute("SELECT id, nombre FROM productos")
        return self.cursor.fetchall()

    def obtener_precio(self, producto_id):
        self.cursor.execute("SELECT precio FROM productos WHERE id = ?", (producto_id,))
        return self.cursor.fetchone()[0]


    def crear_interfaz(self):
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.pack()
        
        self.label_title = tk.Label(self, text="CRUDS de productos", font=("Arial", 20))  # Cambia el tamaño de la letra
        self.label_title.pack()
        
        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.pack()
        
        nombre_label = tk.Label(self, text="Nombre:")
        nombre_label.pack()     
        self.productos = dict(self.obtener_productos())
        self.nombre_combo = ttk.Combobox(self, values=list(self.productos.values()), state="readonly", width=35)
        self.nombre_combo.bind("<<ComboboxSelected>>", self.onChangeComboProductos)
        self.nombre_combo.pack()

        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.pack()

        categoria_label = tk.Label(self, text="Categoría:")
        categoria_label.pack()
        
        self.categorias = dict(self.obtener_categorias())
        self.categoria_combo = ttk.Combobox(self, values=list(self.categorias.values()), state="readonly", width=35)
        self.categoria_combo.pack()

        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.pack()
        
        precio_label = tk.Label(self, text="Precio:")
        precio_label.pack()
        self.precio_entry = tk.Entry(self, validate="key")
        self.precio_entry.config(validatecommand=(self.precio_entry.register(self.validar_precio), '%P'))
        self.precio_entry.pack()

        self.espacio = tk.Label(self, text=" ", font=("Arial", 14))
        self.espacio.pack()
        
        guardar_button = tk.Button(self, text="Actualizar", command=self.guardar_producto)
        guardar_button.pack()
        
        eliminar_button = tk.Button(self, text="Eliminar", command=self.eliminar_producto)
        eliminar_button.pack()
        
        
        self.crear_menu()
        self.mainloop()
        
    def crear_menu(self):
        menu_bar = tk.Menu(self)
        menu_bar.add_command(label="Crear", command=self.registrar_producto)
        self.config(menu=menu_bar)
    
    def registrar_producto(self):
        registrar_producto_window = ViewRegistrarProducto(self)
        registrar_producto_window.focus_set()
        registrar_producto_window.grab_set()
        registrar_producto_window.transient(master=self)
        registrar_producto_window.wait_window()
        
        
    def onChangeComboProductos(self, event):
        nombre = self.nombre_combo.get()
        id = list(self.productos.keys())[list(self.productos.values()).index(nombre)]
        producto = list(self.getProducto(id))
        print(producto)
        self.categoria_combo.set(self.categorias[producto[1]])
        self.precio_entry.delete(0, tk.END)
        self.precio_entry.insert(0, producto[3])
        
       
    def validar_precio(self, valor):
        try:
            float(valor)
            return True
        except ValueError:
            if valor == "":
                return True
            else:
                return False
    
    def getProducto(self, id):
        self.cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
        return self.cursor.fetchone()
    
    def guardar_producto(self):
        nombre = self.nombre_combo.get()
        pid = list(self.productos.keys())[list(self.productos.values()).index(nombre)]
        categoria_id = self.categoria_combo.get()
        precio = float(self.precio_entry.get())
        cid = list(self.categorias.keys())[list(self.categorias.values()).index(categoria_id)]
        self.cursor.execute("UPDATE productos SET categoria_id = ?, precio = ? WHERE id = ?", (cid, precio, pid))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            messagebox.showinfo("Éxito", "Producto actualizado correctamente")
        else:
            messagebox.showerror("Error", "No se pudo actualizar el producto")

    def eliminar_producto(self):
        producto = self.nombre_combo.get()

        if producto == "":
            messagebox.showerror("Error", "No hay un producto seleccionado")
        elif messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar el producto?"):
            try:
                id_prod = list(self.productos.keys())[list(self.productos.values()).index(producto)]
                self.cursor.execute("DELETE FROM productos WHERE id = ?", (id_prod,))
                self.conn.commit()
                messagebox.showinfo("Éxito", "Producto eliminado correctamente")
                self.llenarProductos()
            except Exception as e:
                messagebox.showerror("Error", "Ocurrió un error al eliminar el producto")
    
    def llenarProductos(self):
        self.productos = dict(self.obtener_productos())
        self.nombre_combo.config(values=list(self.productos.values()))
        self.nombre_combo.set("")
        self.categoria_combo.set("")
        self.precio_entry.delete(0, tk.END)

# # Crear una instancia de la clase ViewProductos y ejecutar la interfaz
# view_productos = ViewProductos(None)
