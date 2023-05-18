/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package inicio;

import herramientas.ManipulaArchivos;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import javax.swing.UIManager;

/**
 *
 * @author edenj
 */
public class Inicio {

    public static void main(String[] args) {

        String fecha = (DateTimeFormatter.ofPattern("dd/MM/yyyy")).format(LocalDateTime.now());

        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception ex) {
            System.err.println("Error: " + ex.getMessage());
        }

        String pinAdministrador = "141610";
        double fondoCaja = 1500;
        
        clases.Mesa mesas[] = {
            new clases.Mesa("E1", "", 0, true),
            new clases.Mesa("E2", "", 0, true),
            new clases.Mesa("S1", "", 0, true),
            new clases.Mesa("S2", "", 0, true),
            new clases.Mesa("S3", "", 0, true),
            new clases.Mesa("S4", "", 0, true),
            new clases.Mesa("S5", "", 0, true),
            new clases.Mesa("S6", "", 0, true),
            new clases.Mesa("S1", "", 0, true),
            new clases.Mesa("J1", "", 0, true),
            new clases.Mesa("J2", "", 0, true),
            new clases.Mesa("J3", "", 0, true),};

        String categorias[] = {
            "Desayunos",
            "Para Compartir",
            "Paninis",
            "Crepas Dulces",
            "Crepas Saladas",
            "Ensaladas",
            "Postres",
            "Frappuccinos",
            "Frappes",
            "Malteadas",
            "Fuentes",
            "Expresso",
            "Tizanas",
            "Haz tu desmadre",
            "Desechables",
            "Extras"
        };
        
        ArrayList <clases.Producto> productos = (ArrayList <clases.Producto>) ManipulaArchivos.carga("productos.dat");

        ArrayList <clases.Empleado> empleados = (ArrayList <clases.Empleado>) ManipulaArchivos.carga("empleados.dat");
        
        ArrayList <clases.Venta> venta = (ArrayList <clases.Venta>) ManipulaArchivos.carga("ventas.dat");

//        ManipulaArchivos.guarda("aumento.dat", 0);
        int aumento = (int) ManipulaArchivos.cargaNum("aumento.dat");
        
//        ManipulaArchivos.guarda("folios.dat", 1);
        int folio = (int) ManipulaArchivos.cargaNum("folios.dat");
        
        new ventanas.JFrameInicio(venta, folio, mesas, categorias, productos, empleados, fecha, pinAdministrador, fondoCaja, aumento).setVisible(true);
    }
}
