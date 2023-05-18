/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package clases;

import java.io.Serializable;
import java.util.ArrayList;

/**
 *
 * @author USER
 */
public class Mesa implements Serializable {

    private String nombre;
    private String mesero;
    private int comensales;
    private ArrayList<ProductoVenta> productos;

    /**
     * Constructor de Mesa
     *
     * @param nombre String con el nombre de la mesa.
     * @param abierta boolean que nos muestra el estatus de la mesa. Se genera
     * una lista de ProductoVenta vacia la cual le pertenecerá a la mesa.
     */
    public Mesa(String nombre, String mesero, int comensales, boolean abierta) {
        this.nombre = nombre;
        this.mesero = mesero;
        this.comensales = comensales;
        this.productos = new ArrayList<ProductoVenta>();
    }

    /**
     * @return the nombre
     */
    public String getNombre() {
        return nombre;
    }

    /**
     * @param nombre the nombre to set
     */
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getMesero() {
        return mesero;
    }

    public void setMesero(String mesero) {
        this.mesero = mesero;
    }

    public int getComensales() {
        return comensales;
    }

    public void setComensales(int comensales) {
        this.comensales = comensales;
    }

    /**
     * @return the productos
     */
    public ArrayList<ProductoVenta> getProductos() {
        return productos;
    }

    /**
     * @param productos the productos to set
     */
    public void setProductos(ArrayList<ProductoVenta> productos) {
        this.productos = productos;
    }
}
