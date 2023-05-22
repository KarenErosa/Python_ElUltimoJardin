import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from datetime import date
from productos import Orden
from registrar_empleados import ViewRegistrarTrabajador
import sqlite3
from tkinter import messagebox
from datetime import datetime


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Cafetería")
        self.geometry("1000x600")

        # Connect to SQLite database
        connection = sqlite3.connect("BaseDeDatos/ElUltimoJardin.db")
        cursor = connection.cursor()

        # Fetch usernames from empleados database
        cursor.execute("SELECT username FROM empleados")
        usernames = cursor.fetchall()

        # Close the database connection
        connection.close()

        # Convert the usernames to a list
        usernames = [username[0] for username in usernames]

        # Menu Bar
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        # File Menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Productos", menu=file_menu)
        file_menu.add_command(label="Ver", command=self.open_product_table_window)

        # Edit Menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Empleados", menu=edit_menu)
        edit_menu.add_command(label="Ver", command=self.open_employee_table_window)
        edit_menu.add_command(label="Agregar", command=self.empleados_add)

        # View Menu
        view_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Ventas", menu=view_menu)
        view_menu.add_command(label="Ver", command=self.open_venta_table_window)

        # Transaction Details
        details_frame = ttk.Frame(self)
        details_frame.grid(row=0, column=0, columnspan=4, pady=20)

        fecha_label = ttk.Label(details_frame, text="Fecha:")
        fecha_label.grid(row=0, column=0, sticky="e")

        today = datetime.now().strftime("%d/%m/%Y")
        fecha_valor_label = ttk.Label(details_frame, text=today)
        fecha_valor_label.grid(row=0, column=1, padx=10)

        mesero_label = ttk.Label(details_frame, text="Mesero:")
        mesero_label.grid(row=0, column=2, sticky="e")

        self.mesero_combo = ttk.Combobox(details_frame, values=usernames, state="readonly")
        self.mesero_combo.set(usernames[0] if usernames else "")
        self.mesero_combo.grid(row=0, column=3, padx=10)

        mesa_label = ttk.Label(details_frame, text="Mesa seleccionada:")
        mesa_label.grid(row=1, column=0, sticky="e")

        self.mesa_valor_entry = ttk.Entry(details_frame, state="readonly")
        self.mesa_valor_entry.insert(0, "1")  # Sample mesa number
        self.mesa_valor_entry.grid(row=1, column=1, padx=10)

        mover_mesa_button = ttk.Button(details_frame, text="Mover mesa", command=self.move_table)
        mover_mesa_button.grid(row=1, column=2)

        cantidad_label = ttk.Label(details_frame, text="Cantidad de producto:")
        cantidad_label.grid(row=1, column=3, sticky="e")

        self.cantidad_valor_entry = ttk.Entry(details_frame, state="readonly")
        self.cantidad_valor_entry.insert(0, "1")  # Sample cantidad number
        self.cantidad_valor_entry.grid(row=1, column=4, padx=10)

        cantidad_button = ttk.Button(details_frame, text="Cambiar cantidad", command=self.cambiar_cantidad)
        cantidad_button.grid(row=1, column=5)

        # Transaction Table
        table_frame = ttk.Frame(self)
        table_frame.grid(row=1, column=0, columnspan=4, pady=20)

        self.table = ttk.Treeview(table_frame, columns=("cantidad", "producto", "precio", "total"), show="headings")
        self.table.heading("cantidad", text="Cantidad")
        self.table.heading("producto", text="Producto")
        self.table.heading("precio", text="Precio C/U")
        self.table.heading("total", text="Total")
        self.table.pack(side="left", padx=10)

        # Transaction Buttons and Total
        buttons_frame = ttk.Frame(self)
        buttons_frame.grid(row=2, column=0, columnspan=4, pady=20)

        agregar_button = ttk.Button(buttons_frame, text="Agregar Producto", command=self.add_product)
        agregar_button.pack(side="left", padx=10)

        eliminar_button = ttk.Button(buttons_frame, text="Eliminar Producto", command=self.delete_product)
        eliminar_button.pack(side="left", padx=10)

        venta_button = ttk.Button(buttons_frame, text="Finalizar venta", command=self.venta)
        venta_button.pack(side="left", padx=10)

        total_label = ttk.Label(buttons_frame, text="Total:")
        total_label.pack(side="left", padx=10)

        self.total_valor_label = ttk.Label(buttons_frame, text="0.00")
        self.total_valor_label.pack(side="left")

        # Table Images
        images_frame = ttk.Frame(self)
        images_frame.grid(row=0, column=4, rowspan=3, padx=20, sticky="nsew")

        label_names = ["Mesa 1", "Mesa 2", "Mesa 3", "Mesa 4",
                       "Mesa 5", "Mesa 6", "Mesa 7", "Mesa 8",
                       "Mesa 9", "Mesa 10", "Mesa 11"]
        self.data_table = {
            "Mesa 1" : [],
            "Mesa 2" : [],
            "Mesa 3" : [],
            "Mesa 4" : [],
            "Mesa 5" : [],
            "Mesa 6" : [],
            "Mesa 7" : [],
            "Mesa 8" : [],
            "Mesa 9" : [],
            "Mesa 10" : [],
            "Mesa 11" : []
        }

        self.total_table = {
            "Mesa 1" : 0,
            "Mesa 2" : 0,
            "Mesa 3" : 0,
            "Mesa 4" : 0,
            "Mesa 5" : 0,
            "Mesa 6" : 0,
            "Mesa 7" : 0,
            "Mesa 8" : 0,
            "Mesa 9" : 0,
            "Mesa 10" : 0,
            "Mesa 11" : 0
        }

        for name in label_names:
            label = ttk.Label(images_frame, text=name, relief="solid", width=20)
            label.pack(padx=10, pady=10)
            label.bind("<Button-1>", self.change_color)
        
        self.table.bind('<ButtonRelease-1>', self.on_table_row_click)
    
    def cambiar_cantidad(self):
        try:
            self.data_table[self.mesa_valor_entry.get()]
            selected_item = self.table.focus()  # Get the selected item
            row_data = self.table.item(selected_item)  # Retrieve the row data

            # Retrieve the values of each column
            cantidad = row_data['values'][0]
            producto = row_data['values'][1]
            precio = row_data['values'][2]
            total = row_data['values'][3]
            for data in self.data_table[self.mesa_valor_entry.get()]:
                if(str(data[1]) == str(producto) and str(data[2]) == str(precio) and str(data[3]) == str(cantidad) and str(data[4]) == str(total)):
                    data[3] = self.cantidad_valor_entry.get()
                    num = float(precio)
                    total = num*float(self.cantidad_valor_entry.get())
                    print(self.total_table[self.mesa_valor_entry.get()])
                    self.total_table[self.mesa_valor_entry.get()] -= float(data[4])
                    self.total_table[self.mesa_valor_entry.get()] += float(total)
                    data[4] = total
                    break
            self.clear_table()
        except Exception as e:
            print(str(e))
            messagebox.showerror("Error", f"Datos inválidos o no se ha seleccionado columna")
            
    def on_table_row_click(self, event):
        selected_row = self.table.focus()  # Get the selected row
        if selected_row:  # If a row is selected
            values = self.table.item(selected_row)['values']  # Get the values of the selected row
            first_column_value = values[0]  # Retrieve the value from the first column
            self.cantidad_valor_entry.config(state="normal")  # Enable the entry widget
            self.cantidad_valor_entry.delete(0, 'end')  # Clear the existing value
            self.cantidad_valor_entry.insert(0, first_column_value)  # Insert the new value
            # self.cantidad_valor_entry.config(state="readonly")  # Disable the entry widget

    def llenarEmpleados(self):
         # Connect to SQLite database
        connection = sqlite3.connect("BaseDeDatos/ElUltimoJardin.db")
        cursor = connection.cursor()

        # Fetch usernames from empleados database
        cursor.execute("SELECT username FROM empleados")
        usernames = cursor.fetchall()

        # Close the database connection
        connection.close()

        usernames = [username[0] for username in usernames]

        self.mesero_combo.config(state="normal")
        self.mesero_combo['values'] = ()
        self.mesero_combo['values'] = usernames
        self.mesero_combo.config(state="readonly")

        # Convert the usernames to a list

        self.mesero_combo.set(usernames[0] if usernames else "")

    def open_product_table_window(self):
        # Create a new window
        product_table_window = tk.Toplevel(self)
        product_table_window.title("Tabla de Productos")

        # Create a Treeview widget to display the table
        product_table = ttk.Treeview(product_table_window, columns=("nombre", "precio"), show="headings")
        product_table.heading("nombre", text="Nombre")
        product_table.heading("precio", text="Precio")

        # Connect to the database and retrieve the product data
        try:
            conn = sqlite3.connect("BaseDeDatos/ElUltimoJardin.db")  # Replace with the actual database file name
            cursor = conn.cursor()

            # Retrieve product data from the database
            cursor.execute("SELECT nombre, precio FROM productos")
            rows = cursor.fetchall()

            # Insert the product data into the table
            for row in rows:
                product_table.insert("", "end", values=row)

            conn.close()

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error accessing the database: {str(e)}")

        # Pack the product table
        product_table.pack()

    def open_employee_table_window(self):
        # Create a new window
        product_table_window = tk.Toplevel(self)
        product_table_window.title("Tabla de empleados")

        # Create a Treeview widget to display the table
        product_table = ttk.Treeview(product_table_window, columns=("username", "nombre", "apellido_paterno", "apellido_materno"), show="headings")
        product_table.heading("username", text="username")
        product_table.heading("nombre", text="nombre")
        product_table.heading("apellido_paterno", text="apellido_paterno")
        product_table.heading("apellido_materno", text="apellido_materno")

        # Connect to the database and retrieve the product data
        try:
            conn = sqlite3.connect("BaseDeDatos/ElUltimoJardin.db")  # Replace with the actual database file name
            cursor = conn.cursor()

            # Retrieve product data from the database
            cursor.execute("SELECT username, nombre, apellido_paterno, apellido_materno FROM empleados")
            rows = cursor.fetchall()

            # Insert the product data into the table
            for row in rows:
                product_table.insert("", "end", values=row)

            conn.close()

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error accessing the database: {str(e)}")

        # Pack the product table
        product_table.pack()
    
    def open_venta_table_window(self):
        # Create a new window
        product_table_window = tk.Toplevel(self)
        product_table_window.title("Tabla de Ventas")

        # Create a Treeview widget to display the table
        product_table = ttk.Treeview(product_table_window, columns=("fecha", "hora", "total_venta", "empleado_id"), show="headings")
        product_table.heading("fecha", text="fecha")
        product_table.heading("hora", text="hora")
        product_table.heading("total_venta", text="total_venta")
        product_table.heading("empleado_id", text="empleado_id")

        # Connect to the database and retrieve the product data
        try:
            conn = sqlite3.connect("BaseDeDatos/ElUltimoJardin.db")  # Replace with the actual database file name
            cursor = conn.cursor()

            # Retrieve product data from the database
            cursor.execute("SELECT fecha, hora, total_venta, empleado_id FROM ventas")
            rows = cursor.fetchall()

            # Insert the product data into the table
            for row in rows:
                product_table.insert("", "end", values=row)

            conn.close()

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error accessing the database: {str(e)}")

        # Pack the product table
        product_table.pack()

    def move_table(self):
        # Fetch the selected table number from the entry
        table_number = self.mesa_valor_entry.get()

        # Perform the move table functionality
        # Add your logic here
    def update_table(self, prod_add, totalT):
        # Update the table with prod_add and totalT values
        
        # self.table_values = [prod_add, totalT]
        # self.table_label.config(text=str(self.table_values))
        for prod in prod_add:
            self.data_table[self.mesa_valor_entry.get()].append(prod)
        self.total_table[self.mesa_valor_entry.get()] += totalT
        self.clear_table()
    
    def clear_table(self):
        # Clear the existing rows in the table
        for item in self.table.get_children():
            self.table.delete(item)
        
        # Insert new rows based on the data from prod_add list
        for product in self.data_table[self.mesa_valor_entry.get()]:
            cantidad = product[3]
            producto = product[1]
            precio = product[2]
            total = product[4]
            self.table.insert("", "end", values=(cantidad, producto, precio, total))
        
        # Update the total value
        self.total_valor_label.configure(text=str(self.total_table[self.mesa_valor_entry.get()]))

    def add_product(self):
        orden = Orden(self)  # Create an instance of Orden
        orden.foo()
        orden.mostrar(self)

        # Retrieve the return value from obtener_valor
        prod_add = orden.prod_add
        totalT = orden.totalT

    def delete_product(self):
        selected_item = self.table.focus()  # Get the selected item
        row_data = self.table.item(selected_item)  # Retrieve the row data

        # Retrieve the values of each column
        cantidad = row_data['values'][0]
        producto = row_data['values'][1]
        precio = row_data['values'][2]
        total = row_data['values'][3]
        if selected_item:
            self.table.delete(selected_item) 
        for data in self.data_table[self.mesa_valor_entry.get()]:
            if(str(data[1]) == str(producto) and str(data[2]) == str(precio) and str(data[3]) == str(cantidad) and str(data[4]) == str(total)):
                self.data_table[self.mesa_valor_entry.get()].remove(data)
        self.total_table[self.mesa_valor_entry.get()] -= float(total)
        self.clear_table()
    
    def venta(self):
        
            
        try:
            if self.total_table[self.mesa_valor_entry.get()] != 0:
                # Connect to the database and retrieve the product data
                conn = sqlite3.connect("BaseDeDatos/ElUltimoJardin.db")  # Replace with the actual database file name
                cursor = conn.cursor()

                    # Retrieve product data from the database
                cursor.execute("SELECT id FROM empleados WHERE username = ?", (self.mesero_combo.get(),))
                row = cursor.fetchone() 
                empleado_id = row[0]
                fecha = datetime.now().strftime("%d/%m/%Y")
                hora = datetime.now().strftime("%H:%M:%S")
                total_venta = self.total_table[self.mesa_valor_entry.get()]
                # for item in self.table.get_children():
                #     values = self.table.item(item)['values']
                #     print(values)
                cursor.execute("INSERT INTO ventas (fecha, hora, total_venta, empleado_id) VALUES (?, ?, ?, ?)", (fecha, hora, total_venta, empleado_id))
                conn.commit()
                conn.close()
                messagebox.showinfo("Venta", "Venta registrada")
                self.total_table[self.mesa_valor_entry.get()] = 0
                self.total_table[self.mesa_valor_entry.get()]
                self.data_table[self.mesa_valor_entry.get()] = []
                self.clear_table()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error accessing the database: {str(e)}")
         
        
            

    def change_color(self,event):
        label = event.widget  # Get the label widget that triggered the event
        self.mesa_valor_entry.config(state="normal")  # Set the entry field to normal state
        self.mesa_valor_entry.delete(0, tk.END)  # Clear the current input value
        self.mesa_valor_entry.insert(0, label["text"])  # Set the clicked label's text as the input value
        self.mesa_valor_entry.config(state="readonly")  # Set the 
        self.clear_table()
    
    def empleados_add(self):
        empleados = ViewRegistrarTrabajador(self)
        empleados.mainloop()

# Create an instance of the MainWindow class and run the application
if __name__ == "__main__":
    app = MainWindow()
    app.mesa_valor_entry.config(state="normal")
    app.mesa_valor_entry.delete(0, tk.END)
    app.mesa_valor_entry.insert(0, 'Mesa 1')
    app.mesa_valor_entry.config(state="readonly")
    app.mainloop()
    



