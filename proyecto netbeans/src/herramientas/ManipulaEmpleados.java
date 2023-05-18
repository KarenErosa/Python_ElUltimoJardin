/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package herramientas;

import clases.Empleado;
import java.awt.event.KeyEvent;
import java.util.ArrayList;
import javax.swing.JComboBox;
import javax.swing.JOptionPane;
import javax.swing.JTable;

/**
 *
 * @author USER
 */
public class ManipulaEmpleados {
    public static void llenarCombo(ArrayList <clases.Empleado> empleados, JComboBox jbox) {
        jbox.removeAllItems();
        if (empleados != null) {
            for (Empleado empleado : empleados) {
                jbox.addItem(empleado.getNombre());
            }   
        }
    }
    
    public static boolean CalculaRetardo(String hora1, String hora2){
        if (hora1.charAt(0) > hora2.charAt(0)) {
            return false;
        }
        if (hora1.charAt(0) < hora2.charAt(0)) {
            return true;
        } else {
            if (hora1.charAt(1) > hora2.charAt(1)) {
                return false;
            } else {
                if (hora1.charAt(3) > hora2.charAt(3)) {
                    return false;
                }
                if (hora1.charAt(3) < hora2.charAt(3)) {
                    return true;
                } else {
                    if (hora1.charAt(4) > hora2.charAt(4)) {
                        return false;
                    } else {
                        if (hora1.charAt(4) == hora2.charAt(4)) {
                            return false;
                        }else{
                            return true;
                        }
                    }
                }
            }
        }
    }
    
    
    public static boolean ingresarEmpleado(ArrayList <clases.Empleado> empleados, String nombre, int pin, String hora) {
        if (empleados != null) {
            for (Empleado empleado : empleados) {
                if (empleado.getNombre().equals(nombre)) {
                    if (empleado.getPin() == pin) {
                        empleado.setIngreso(true);
                        if (CalculaRetardo(empleado.getHoraEntrada(), hora)) {
                            empleado.setRetardos(empleado.getRetardos()+1);
                        }
                        return true;
                    }
                }
            }
        }
        return false;
    }
    
    public static int ConsultaRetardos(ArrayList <clases.Empleado> empleados, String nombre) {
        if (empleados != null) {
            for (Empleado empleado : empleados) {
                if (empleado.getNombre().equals(nombre)){
                    return empleado.getRetardos();
                }
            }
        }
        return 0;
    }
    
    public static boolean ConsultaIngreso(ArrayList <clases.Empleado> empleados, String nombre) {
        if (empleados != null) {
            for (Empleado empleado : empleados) {
                if (empleado.getNombre().equals(nombre)){
                    if (empleado.getIngreso()) {
                        return true;
                    }else{
                        return false;
                    }
                }
            }
        }
        return false;
    }
    
    public static String encriptar(String cadena) {
        String str = "";
        int tamano = cadena.length();
        if (tamano >= 0) {
            for (int i = 0; i < tamano; i++) {
                str = str + "*";
            }
            return str;
        }
        return cadena;
    }
    
    public static Empleado buscaEmpleado(ArrayList<clases.Empleado> empleados, String nombre) {
        if (empleados != null) {
            for (Empleado emp1 : empleados) {
                if (emp1.getNombre().equals(nombre)) {
                    return emp1;
                }
            }
        }
        return null;
    }
}
