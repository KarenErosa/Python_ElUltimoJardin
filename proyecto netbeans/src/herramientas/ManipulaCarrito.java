/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package herramientas;

import clases.Empleado;
import clases.Producto;
import java.util.ArrayList;
import javax.swing.JComboBox;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author edenj
 */
public class ManipulaCarrito {

    /**
     * Método que nos permite mostrar los elementos de un ArrayList en una
     * JTable
     *
     * @param tabla JTable en las que se mostrará la lista de los productos que
     * estan en el ArrayList.
     * @param productos ArrayList<clases.ProductoVenta> de productos que se
     * desean mostrar en el JTable.
     * @return Double con el valor total (cantidad * precioUnitario) de todos
     * los productos que hay en la lista mostrada en el JTable, no es necesario
     * usarlo, pero se deja por si es necesaria su implementación.
     */
    public static double mostrarProducto(JTable tabla, ArrayList<clases.ProductoVenta> productos) {
        DefaultTableModel modelo = (DefaultTableModel) tabla.getModel();
        modelo.setNumRows(0);
        if (!productos.isEmpty()) {
            double totalProductos = 0;
            for (clases.ProductoVenta producto : productos) {
                int cantidad = producto.getCantidad();
                String nombre = producto.getNombreProducto();
                double precio = producto.getPrecio();
                double total = cantidad * precio;
                totalProductos += total;
                String matrizDetalle[] = {"" + cantidad, nombre, "" + precio, "$ " + total};
                modelo.addRow(matrizDetalle);
            }
            return totalProductos;
        }
        return 0;
    }
    

    /**
     * Método que nos permite llenar un JComboBox con un arreglo de String
     *
     * @param categorias String[] con los elementos a agregar al JComboBox
     * @param jbox JComboBox en el que se desea agregar los elementos. Como nota
     * adicional se eliminan los elementos que tenía el jbox y se agregan los
     * nuevos.
     */
    public static void llenarCombo(String categorias[], JComboBox jbox) {
        jbox.removeAllItems();
        if (categorias != null) {
            for (String categoria : categorias) {
                jbox.addItem(categoria);
            }
        }
    }
    


    /**
     * Método que nos permite llenar un JTable con los productos de cierta
     * categoría.
     *
     * @param categoria String con la categoría de los productos que se desean
     * mostrar.
     * @param jtproductos JTable en el que se agregarán los productos de la
     * categoría dada.
     * @param productos clases.Producto[] que contiene una lista de todos los
     * productos en general.
     */
    public static void obtenerProductoCategoria(String categoria, JTable jtproductos, ArrayList <clases.Producto> productos) {
        if (productos != null) {
            DefaultTableModel modelo = limpiarFilasJTable(jtproductos);
            for (Producto producto : productos) {
                if (producto.getCategoria().toLowerCase().equals(categoria.toLowerCase())) {
                    modelo.addRow(new Object[]{producto.getNombreProducto(), producto.getPrecio()});
                }
            }
        }
    }

    /**
     * Método que nos permite eliminar todo el contenido de un JTable,
     * eliminando todas las filas.
     *
     * @param jTable JTable que se desea limpiar.
     * @return DefaultTableModel del modelo ya limpio, no es necesario ponerlo
     * pero se deja por si se ocupa como referencia.
     */
    public static DefaultTableModel limpiarFilasJTable(JTable jTable) {
        DefaultTableModel modelo = (DefaultTableModel) jTable.getModel();
        modelo.setNumRows(0);
        return modelo;
    }

    /**
     * Método que nos permite obtener la posición de un producto en un JTable.
     *
     * @param tabla JTable en el que se buscará el producto.
     * @param cadena String con la cadena a buscar.
     * @return Int con la posción de la fila en donde se encontró el producto,
     * en caso de no encontrarlo un -1.
     */
    public static int buscaProducto(JTable tabla, String cadena) {
        cadena = (cadena).toUpperCase();
        for (int i = 0; i < tabla.getRowCount(); i++) {
            if (((String) tabla.getValueAt(i, 0)).length() >= cadena.length()) {
                if ((((String) tabla.getValueAt(i, 0)).substring(0, cadena.length()).toUpperCase()).equals(cadena)) {
                    tabla.changeSelection(i, 1, false, false);
                    return i;
                }
            }
        }
        return -1;
    }
    
    public static clases.Producto buscaNombreProducto(ArrayList <clases.Producto> productos, String cadena) {
        for (Producto producto : productos) {
            if (producto.getNombreProducto().equals(cadena)) {
                return producto;
            }
        }
        return null;
    }
}
