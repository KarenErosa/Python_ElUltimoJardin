/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package herramientas;

import clases.Mesa;

/**
 *
 * @author edenj
 */
public class ManipulaMesas {

    /**
     * Método que nos permite obtener el objeto mesa de acuerdo al nombre de est
     *
     * @param mesas clases.Mesa[] con el arreglo de mesas en donde buscaremos.
     * @param nombre String con el nombre de la mesa a buscar.
     * @return Objeto Mesa o en caso de no encontrarla un null.
     */
    public static clases.Mesa obtenerMesa(clases.Mesa mesas[], String nombre) {
        for (clases.Mesa mesa : mesas) {
            if (mesa.getNombre().equals(nombre)) {
                return mesa;
            }
        }
        return null;
    }

    /**
     * Método que nos permite obtener la posición de un producto de la lista de
     * una mesa.
     *
     * @param mesa Mesa de la que obtenedremos la lista de ProductosVenta.
     * @param nombreProducto String con el nombre del producto a buscar.
     * @return Int con la posición del producto dentro de la lista de la mesa,
     * en caso de no encontrar -1.
     */
    public static int posProducto(clases.Mesa mesa, String nombreProducto) {
        int indice = -1;
        for (clases.ProductoVenta producto : mesa.getProductos()) {
            indice++;
            if (producto.getNombreProducto().equals(nombreProducto)) {
                return indice;
            }
        }
        return -1;
    }
}
