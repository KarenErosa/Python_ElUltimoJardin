
import sqlite3
import tkinter as tk
from tkinter import ttk

prod_add=[]
totalT=0
conn=None
try:
    conn=sqlite3.connect('BaseDeDatos/ElUltimoJardin.db')
except:
    print('No se conecto a la base de datos')

cur=conn.cursor()
cur.execute("SELECT id,nombre,precio,categoria_id FROM productos")

datos=cur.fetchall()

products=[]

for dato in datos:
    col={"id":dato[0],"producto":dato[1],"precio":dato[2],"categoria":dato[3]}
    products.append(col)

# Sample data for the food products and prices


def agregar():
    global totalT
    selected_product = table.focus()
    if selected_product:
        producto=table.item(selected_product)
        valores=producto['values']
        cantidad = cantidad_entry.get()
        precio=float(valores[2])

    try:
        cant=float(cantidad)

        if cant>0:
            total =  cant* precio
            valores.append(cantidad)
            valores.append(total)
            # Calculate the total
            i=0
            bnd=True
            while bnd and i<len(prod_add):
                if prod_add[i][0]==valores[0]:
                    bnd=False
                i+=1

            if bnd:
                prod_add.append(valores)
            else:
                i-=1
                totalT-=prod_add[i][4]
                prod_add[i][3]=cantidad
                prod_add[i][4]=total

            print(prod_add)
            totalT+=total
            # Display the total
            total_label.config(text=f"Total: ${totalT:.2f}")

            # Add code here to perform any other actions you need when "Agregar" button is clicked
    except Exception as e:
        print(e)


def search_product():
    search_query = producto_entry.get().lower()
    matching_products = [product for product in products if search_query in product["producto"].lower()]

    # Clear the existing table
    table.delete(*table.get_children())

    # Insert matching products into the table
    for product in matching_products:
        table.insert("", "end", values=(product["producto"], product["precio"]))


def obtener_valor():
    global totalT
    window.destroy()  # Cierra la ventana actual al obtener el valor
    return prod_add,totalT

# Create the Tkinter window
window = tk.Tk()
window.title("Orden")

# Create a search bar for product search
producto_label = ttk.Label(window, text="Producto:")
producto_label.pack()

producto_entry = ttk.Entry(window)
producto_entry.pack()

search_button = ttk.Button(window, text="Buscar", command=search_product)
search_button.pack()

# Create a combobox for selecting the food category
combo_label = ttk.Label(window, text="Categoría:")
combo_label.pack()

cur.execute("SELECT id,nombre FROM categorias")

datos=cur.fetchall()

categorias=[('Todo',0)]

for dato in datos:
    col=(dato[1],dato[0])
    categorias.append(col)

def on_option_selected(event):
    index = combo.current()
    assigned_value = categorias[index][1]

    # Clear the existing table
    table.delete(*table.get_children())

    # Insert matching products into the table
    if assigned_value!=0:
        for product in products:
            if product["categoria"]==assigned_value:
                table.insert("", "end", values=(product["id"],product["producto"], product["precio"]))
    else:
        for product in products:
            table.insert("", "end", values=(product["id"],product["producto"], product["precio"]))

combo_text = [option[0] for option in categorias]
combo = ttk.Combobox(window, values=combo_text)
combo.pack()

combo.set('Todo')

combo.option_add("*TCombobox*Listbox.selectBackground", "lightblue")

combo.bind('<<ComboboxSelected>>',on_option_selected)

# Create a table to display the products and prices
table = ttk.Treeview(window, columns=("id","producto", "precio"), show="headings", displaycolumns=("1","2"))
table.heading("producto", text="Producto")
table.heading("precio", text="Precio")

for product in products:
    table.insert("", "end", values=(product["id"],product["producto"], product["precio"]))

table.pack()

# Create a field for entering the quantity
cantidad_label = ttk.Label(window, text="Cantidad:")
cantidad_label.pack()
cantidad_entry = ttk.Entry(window)
cantidad_entry.pack()

# Create a label to display the total
total_label = ttk.Label(window, text="Total: $0.00")
total_label.pack()

# Create a button to add the item
agregar_button = ttk.Button(window, text="Agregar", command=agregar)
agregar_button.pack()

# Start the Tkinter event loop
window.mainloop()

total_label = ttk.Label(window, text="Total: $0.00")
total_label.pack()

# Create a button to add the item
agregar_button = ttk.Button(window, text="Agregar", command=agregar)
agregar_button.pack()

boton = tk.Button(window, text="Confirmar", command=obtener_valor)
boton.pack()

# Start the Tkinter event loop
window.mainloop()

