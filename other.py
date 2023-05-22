import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from datetime import date
import sqlite3

def open_product_table_window():
    # Create a new window
    product_table_window = tk.Toplevel(window)
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

def open_employee_table_window():
    # Create a new window
    product_table_window = tk.Toplevel(window)
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

def move_table():
    # Add code here to handle the "Mover Mesa" button functionality
    pass

def add_product():
    # Add code here to handle the "Agregar Producto" button functionality
    pass

def delete_product():
    # Add code here to handle the "Eliminar Producto" button functionality
    pass

def change_color(event):
    label = event.widget  # Get the label widget that triggered the event
    mesa_valor_entry.config(state="normal")  # Set the entry field to normal state
    mesa_valor_entry.delete(0, tk.END)  # Clear the current input value
    mesa_valor_entry.insert(0, label["text"])  # Set the clicked label's text as the input value
    mesa_valor_entry.config(state="readonly")  # Set reqadonly again




# Create the Tkinter window
window = tk.Tk()
window.title("Cafetería")
window.geometry("1000x600")

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
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="Productos")
# file_menu.add_command(label="Empleados")
# file_menu.add_separator()
# file_menu.add_command(label="Salir", command=window.quit)
menu_bar.add_cascade(label="Productos", menu=file_menu)
file_menu.add_command(label="Productos", command=open_product_table_window)

# Edit Menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
# edit_menu.add_command(label="Cut")
# edit_menu.add_command(label="Copy")
# edit_menu.add_command(label="Paste")
menu_bar.add_cascade(label="Empleados", menu=edit_menu)
edit_menu.add_command(label="Empleados", command=open_employee_table_window)

# View Menu
view_menu = tk.Menu(menu_bar, tearoff=0)
# view_menu.add_command(label="View 1")
# view_menu.add_command(label="View 2")
menu_bar.add_cascade(label="Ventas", menu=view_menu)

# Transaction Details
details_frame = ttk.Frame(window)
details_frame.grid(row=0, column=0, columnspan=4, pady=20)

fecha_label = ttk.Label(details_frame, text="Fecha:")
fecha_label.grid(row=0, column=0, sticky="e")

today = date.today().strftime("%d/%m/%Y")
fecha_valor_label = ttk.Label(details_frame, text=today)
fecha_valor_label.grid(row=0, column=1, padx=10)

mesero_label = ttk.Label(details_frame, text="Mesero:")
mesero_label.grid(row=0, column=2, sticky="e")

mesero_combo = ttk.Combobox(details_frame, values=usernames, state="readonly")
mesero_combo.set(usernames[0] if usernames else "")  # Set the first username as default if available
mesero_combo.grid(row=0, column=3, padx=10)

mesa_label = ttk.Label(details_frame, text="Mesa seleccionada:")
mesa_label.grid(row=1, column=0, sticky="e")

mesa_valor_entry = ttk.Entry(details_frame, state="readonly")
mesa_valor_entry.insert(0, "1")  # Sample mesa number
mesa_valor_entry.grid(row=1, column=1, padx=10)

mover_mesa_button = ttk.Button(details_frame, text="Mover Mesa", command=move_table)
mover_mesa_button.grid(row=1, column=2)

# Transaction Table
table_frame = ttk.Frame(window)
table_frame.grid(row=1, column=0, columnspan=4, pady=20)

table = ttk.Treeview(table_frame, columns=("cantidad", "producto", "precio", "total"), show="headings")
table.heading("cantidad", text="Cantidad")
table.heading("producto", text="Producto")
table.heading("precio", text="Precio C/U")
table.heading("total", text="Total")
table.pack(side="left", padx=10)

# Transaction Buttons and Total
buttons_frame = ttk.Frame(window)
buttons_frame.grid(row=2, column=0, columnspan=4, pady=20)

agregar_button = ttk.Button(buttons_frame, text="Agregar Producto", command=add_product)
agregar_button.pack(side="left", padx=10)

eliminar_button = ttk.Button(buttons_frame, text="Eliminar Producto", command=delete_product)
eliminar_button.pack(side="left", padx=10)

total_label = ttk.Label(buttons_frame, text="Total:")
total_label.pack(side="left", padx=10)

total_valor_label = ttk.Label(buttons_frame, text="0.00")
total_valor_label.pack(side="left")

# Table Images
images_frame = ttk.Frame(window)
images_frame.grid(row=0, column=4, rowspan=3, padx=20, sticky="nsew")

label_names = ["Mesa 1", "Mesa 2", "Mesa 3", "Mesa 4",
"Mesa 5", "Mesa 6", "Mesa 7", "Mesa 8",
"Mesa 9", "Mesa 10", "Mesa 11"]

for name in label_names:
    label = ttk.Label(images_frame, text=name, relief="solid", width=20)
    label.pack(padx=10, pady=10)
    label.bind("<Button-1>", change_color)

window.mainloop()


