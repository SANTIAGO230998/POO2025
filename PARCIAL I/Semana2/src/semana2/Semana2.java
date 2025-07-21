/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package semana2;

/**
 *
 * @author SANTI
 */
public class Semana2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        /// Creamos objetos de tipo Animal utilizando las clases hijas (polimorfismo)
        Animal perro = new Perro("El perro Romel", 3);  // Crea un objeto Perro
        Animal gato = new Gato("El gato Misael", 2);    // Crea un objeto Gato
        Animal vaca = new Vaca("La vaca Lola", 4);      // Crea un objeto Vaca

         // Llamamos al método hacerSonido() en cada objeto
        // Cada objeto responde de forma diferente (polimorfismo)
        perro.hacerSonido();    // Imprime "El perro Romel dice: Guau gau!"
        gato.hacerSonido();     // Imprime "El gato Misael dice: Miau!"
        vaca.hacerSonido();     // Imprime "La vaca Lola dice: muuuuu!"

        // Mostramos la información de cada animal usando los métodos get (encapsulación)
        System.out.println(perro.getNombre() + " tiene " + perro.getEdad() + " anios.");
        System.out.println(gato.getNombre() + " tiene " + gato.getEdad() + " anios.");
        System.out.println(vaca.getNombre() + " tiene " + vaca.getEdad() + " anios.");
    }
}