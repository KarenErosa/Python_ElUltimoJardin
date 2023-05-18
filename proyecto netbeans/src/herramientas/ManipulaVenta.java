/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package herramientas;

import clases.Venta;
import java.util.ArrayList;
import javax.swing.JComboBox;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;


/**
 *
 * @author USER
 */
public class ManipulaVenta {
    
    public static String mostrarProducto(ArrayList<clases.ProductoVenta> productos) {
        if (!productos.isEmpty()) {
            String tmp = "";
            for (clases.ProductoVenta producto : productos) {
                int cantidad = producto.getCantidad();
                String nombre = producto.getNombreProducto();
                double precio = producto.getPrecio();
                double total = cantidad * precio;
                tmp = tmp + "" + cantidad + " " + rellenar(nombre) + "$" + precio + "   $" + total + "\n";
            }
            return tmp;
        }
        return "";
    }
    
    public static String rellenar(String texto){
        if (texto.length() < 25) {
            int cantidad = 25 - texto.length();
            while(cantidad > 0){
                texto = texto +" ";
                cantidad--;
            }
            return texto;
        }
        return "";
    }
    
    public static String venta(clases.Venta venta){
        String texto="El último Jardín \n -Café- \n";
        texto = texto +
                "Folio: " + venta.getFolio() + "\n" +
                "Fecha: " + venta.getFecha() + "\tHora: " + venta.getHora() + "\n" +
                "Mesa: \"" + venta.getMesa().getNombre() + "\"\t\tMesero: " + venta.getMesa().getMesero() + "\n\n";
        texto = texto + "C Producto\t\tPrecioC/U  Total \n";
        texto = texto + mostrarProducto(venta.getMesa().getProductos());
        texto = texto + "\n" +
                "Total\t\t\t\t   $" + venta.getTotal() + "\n" ;
                
        return texto;
    }
    
    public static String nota(String texto){
        texto = texto + "\n" +
                "-------------------------------------------\n" + 
                "¿Cómo te atendimos? \n"
                +"https://www.facebook.com/ElultimoJardinCafe \n\n" + 
                "Ven por un lugar agradable y especial, \nquédate por el producto delicioso \ny de calidad, en \"El último Jardín café\""
                + "\n\nESTE COMPROBANTE NO ES \nVALIDO PARA EFECTOS FISCALES \n\n"
                + "SI REQUIERES FACTURA SOLICITALA \nEL MISMO DIA DE LA COMPRA, EN CAJA\n\n"
                + "ESTA NOTA, ES PARTE INTEGRA \nDE LA VENTA DEL DIA \n";
                
        return texto;
    }
    
    public static void llenarFechas(ArrayList<clases.Venta> ventas, JComboBox fecha){
        String tmp = "";
        if (ventas.size() > 0) {
            for (Venta venta : ventas) {
                if (!tmp.equals((String) venta.getFecha())) {
                    tmp = (String) venta.getFecha();
                    fecha.addItem(tmp);
                }
            }
        }
    }
    
    public static void mostrarVentas(JTable tabla, ArrayList<clases.Venta> ventas, String fecha) {
        DefaultTableModel modelo = (DefaultTableModel) tabla.getModel();
        modelo.setNumRows(0);
        if (!ventas.isEmpty()) {
            int numero = 1;
            for (Venta venta : ventas) {
                if (venta.getFecha().equals(fecha)) {
                    String hora = venta.getHora();
                    String mesa = venta.getMesa().getNombre();
                    String mesero = venta.getMesa().getMesero();
                    String total = venta.getTotal();
                    String matrizDetalle[] = {String.valueOf(numero), hora, mesa, mesero, "$ " + total};
                    modelo.addRow(matrizDetalle);
                    numero++;
                }
            }
        }
    }
}
