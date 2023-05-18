package clases;

import java.io.Serializable;

/**
 *
 * @author Sofia Erosa
 */
public class Producto implements Serializable{

    private String nombreProducto;
    private String categoria;
    private double precio;

    /**
     * Constructor de Productos
     *
     * @param nombreProducto String que contiene el nombre del producto.
     * @param categoria String que contiene la categoría al que pertenece este
     * producto.
     * @param precio Double que contiene el precio unitario del producto.
     */
    public Producto(String nombreProducto, String categoria, double precio) {
        this.nombreProducto = nombreProducto;
        this.categoria = categoria;
        this.precio = precio;
    }

    /**
     * @return the nombreProducto
     */
    public String getNombreProducto() {
        return nombreProducto;
    }

    /**
     * @param nombreProducto the nombreProducto to set
     */
    public void setNombreProducto(String nombreProducto) {
        this.nombreProducto = nombreProducto;
    }

    /**
     * @return the categoria
     */
    public String getCategoria() {
        return categoria;
    }

    /**
     * @param categoria the categoria to set
     */
    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    /**
     * @return the precio
     */
    public double getPrecio() {
        return precio;
    }

    /**
     * @param precio the precio to set
     */
    public void setPrecio(double precio) {
        this.precio = precio;
    }

}
