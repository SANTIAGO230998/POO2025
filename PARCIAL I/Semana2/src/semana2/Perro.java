/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package semana2;

/**
 *
 * @author SANTI
 */
// Declaración de la clase Perro que extiende la clase Animal
public class Perro extends Animal {
    // Constructor de la clase Perro, recibe nombre y edad como parámetros
    public Perro(String nombre, int edad) {
        // Llama al constructor de la clase padre (Animal) para asignar nombre y edad
        super(nombre, edad);
    }

    // Sobrescribe el método abstracto hacerSonido() de la clase Animal
    // Este es un ejemplo de polimorfismo, ya que cada animal define su propia versión del método
    @Override
    public void hacerSonido() {
        // Imprime el sonido característico del perro, junto con su nombre
        System.out.println(getNombre() + " dice: Guau gau!");
    }
}