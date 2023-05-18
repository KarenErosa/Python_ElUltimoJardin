
package clases;

import java.io.Serializable;

public class Empleado implements Serializable{
    String nombre;
    boolean ingreso;
    int pin;
    String horaEntrada;
    String horaLimite;
    int retardos;

    public Empleado() {
    }

    public Empleado(String nombre, boolean ingreso, int pin, String horaEntrada, String horaLimite, int retardos) {
        this.nombre = nombre;
        this.ingreso = ingreso;
        this.pin = pin;
        this.horaEntrada = horaEntrada;
        this.horaLimite = horaLimite;
        this.retardos = retardos;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public boolean getIngreso() {
        return ingreso;
    }

    public void setIngreso(boolean ingreso) {
        this.ingreso = ingreso;
    }

    public int getPin() {
        return pin;
    }

    public void setPin(int pin) {
        this.pin = pin;
    }

    public String getHoraEntrada() {
        return horaEntrada;
    }

    public void setHoraEntrada(String horaEntrada) {
        this.horaEntrada = horaEntrada;
    }

    public String getHoraLimite() {
        return horaLimite;
    }

    public void setHoraLimite(String horaLimite) {
        this.horaLimite = horaLimite;
    }

    public int getRetardos() {
        return retardos;
    }

    public void setRetardos(int retardos) {
        this.retardos = retardos;
    }
    
    
    
    
}
