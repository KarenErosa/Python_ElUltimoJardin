/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package herramientas;

import javax.swing.JFrame;
import javax.swing.JPanel;

/**
 *
 * @author edenj
 */
public class HerramientasInterfaz {
    /**
     * Método que pone un JPanel en un JFrame;
     *
     * @param ventana JFrame donde se pondra el JPanel;
     * @param titulo String que le da titulo a la ventana;
     * @param panel JPanel que se desea agregar;
     * @param centro boolean true si se quiere poner la ventana al centro, en
     * caso contrario false;
     */
    public static void addPanel(JFrame ventana, JPanel panel, String titulo, boolean centro) {
        ventana.setTitle(titulo);
        ventana.setContentPane(panel);
        if (centro) {
            ventana.setLocationRelativeTo(null);
        }
        ventana.setVisible(true);
    }
}
