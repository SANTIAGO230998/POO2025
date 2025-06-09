/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package semana2;

/**
 *
 * @author SANTI
 */
// Declaración de la clase Gato que extiende (hereda de) la clase Animal
public class Gato extends Animal {
    
    // Constructor de la clase Gato, recibe nombre y edad como parámetros
    public Gato(String nombre, int edad) {
        // Llama al constructor de la clase padre (Animal) para inicializar los atributos
        super(nombre, edad);
    }

    // Sobrescritura del método abstracto hacerSonido de la clase Animal
    // Esto es un ejemplo de polimorfismo: el Gato tiene su propia versión del método
    @Override
    public void hacerSonido() {
        // Imprime el sonido específico que hace el gato, junto con su nombre
        System.out.println(getNombre() + " dice: Miau!");
    }
}
