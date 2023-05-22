/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ventanas;

import clases.Empleado;
import herramientas.ManipulaEmpleados;
import java.util.ArrayList;
import javax.swing.JOptionPane;

/**
 *
 * @author USER
 */
public class JDialogPagoNomina extends javax.swing.JDialog {

    ArrayList <clases.Empleado> empleados;
    ArrayList <clases.Venta> ventas;
    /**
     * Creates new form JDialogPagoNomina
     */
    public JDialogPagoNomina(java.awt.Frame parent, boolean modal,  ArrayList <clases.Empleado> empleados, ArrayList <clases.Venta> ventas) {
        super(parent, modal);
        this.empleados = empleados;
        this.ventas = ventas;
        initComponents();
        jTextAreaRegistros.setText(escribe(empleados));
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jButtonreinicioSemanal = new javax.swing.JButton();
        jScrollPane1 = new javax.swing.JScrollPane();
        jTextAreaRegistros = new javax.swing.JTextArea();

        setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);

        jButtonreinicioSemanal.setText("Reinicio Semanal");
        jButtonreinicioSemanal.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonreinicioSemanalActionPerformed(evt);
            }
        });

        jTextAreaRegistros.setColumns(20);
        jTextAreaRegistros.setRows(5);
        jScrollPane1.setViewportView(jTextAreaRegistros);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addGap(0, 0, Short.MAX_VALUE)
                        .addComponent(jButtonreinicioSemanal))
                    .addComponent(jScrollPane1, javax.swing.GroupLayout.DEFAULT_SIZE, 380, Short.MAX_VALUE))
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jScrollPane1, javax.swing.GroupLayout.DEFAULT_SIZE, 237, Short.MAX_VALUE)
                .addGap(18, 18, 18)
                .addComponent(jButtonreinicioSemanal)
                .addContainerGap())
        );

        pack();
        setLocationRelativeTo(null);
    }// </editor-fold>//GEN-END:initComponents

    private void jButtonreinicioSemanalActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButtonreinicioSemanalActionPerformed
        int confirm = 1;
        if (empleados.size() > 0) {
            confirm = JOptionPane.showConfirmDialog(null, 
                    ("¿Desea reiniciar el registro semanal?\nEsto eliminara:\n Los retardos registrados \nLas ventas realizadas hasta el momento"),
                    "Confirmación de Pago de Nomina", 
                    JOptionPane.YES_NO_OPTION, 
                    JOptionPane.WARNING_MESSAGE);
        }
        if (confirm == 0) {
            for (Empleado empleado : empleados) {
                empleado.setRetardos(0);
            }
            ventas.removeAll(ventas);
            JOptionPane.showMessageDialog(this, "Registros reiniciados");
        }
        jTextAreaRegistros.setText(escribe(empleados));
    }//GEN-LAST:event_jButtonreinicioSemanalActionPerformed

    public static String escribe(ArrayList <clases.Empleado> empleados){
        String texto = "";
        if (empleados.size() > 0) {
            for (Empleado empleado : empleados) {
                String nombre = "Nombre: " + empleado.getNombre();
                String ingreso;
                if (empleado.getIngreso()) {
                    ingreso = "\nStatus: El empleado ya ha entrado a turno";
                } else {
                    ingreso = "\nStatus: El empleado aun no ha entrado a turno";
                }
                String horaEntrada = "\nHora de Entrada: " + empleado.getHoraEntrada();
                String horaLimite = "\nHora Limite de entrada: " + empleado.getHoraLimite();
                String retardos = "\nRetardos semanales: " + String.valueOf(empleado.getRetardos()) +"\n\n";
                texto = texto+(nombre + ingreso + horaEntrada + horaLimite + retardos);
            }
            return texto;
        }
        return "";
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton jButtonreinicioSemanal;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTextArea jTextAreaRegistros;
    // End of variables declaration//GEN-END:variables
}