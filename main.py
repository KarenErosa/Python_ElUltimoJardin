
import tkinter as tk
from tkinter import ttk

# Sample data for the food products and prices
products = [
    {"producto": "Huevos al gusto", "precio": 25.0},
    {"producto": "Pan dulce", "precio": 6.0},
    {"producto": "Leche", "precio": 12.0},
    {"producto": "Pollo", "precio": 15.0},
    {"producto": "Panqueques", "precio": 30.0},
    {"producto": "Malteada Yakult", "precio": 55.0},
    {"producto": "Galletas de chocolate", "precio": 10.0},
    {"producto": "Galletas Red Velvet", "precio": 6.0},
    # Add more products as needed
]


def agregar():
    selected_product = combo.get()
    cantidad = cantidad_entry.get()

    # Retrieve the price of the selected product
    precio = next(item["precio"] for item in products if item["producto"] == selected_product)

    # Calculate the total
    total = float(cantidad) * precio

    # Display the total
    total_label.config(text=f"Total: ${total:.2f}")

    # Add code here to perform any other actions you need when "Agregar" button is clicked


def search_product():
    search_query = producto_entry.get().lower()
    matching_products = [product for product in products if search_query in product["producto"].lower()]

    # Clear the existing table
    table.delete(*table.get_children())

    # Insert matching products into the table
    for product in matching_products:
        table.insert("", "end", values=(product["producto"], product["precio"]))


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

combo = ttk.Combobox(window, values=["Desayuno", "Comida", "Cena"])
combo.pack()

# Create a table to display the products and prices
table = ttk.Treeview(window, columns=("producto", "precio"), show="headings")
table.heading("producto", text="Producto")
table.heading("precio", text="Precio")

for product in products:
    table.insert("", "end", values=(product["producto"], product["precio"]))

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

# Start the Tkinter event loop
window.mainloop()

