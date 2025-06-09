/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package semana2;

/**
 *
 * @author SANTI
 */
// Declaración de la clase Vaca que extiende (hereda de) la clase Animal
public class Vaca extends Animal {
    // Constructor de la clase Vaca, recibe el nombre y la edad como parámetros
    public Vaca(String nombre, int edad) {
        // Llama al constructor de la clase padre (Animal) para inicializar los atributos
        super(nombre, edad);
    }

    // Sobrescribe el método abstracto hacerSonido() definido en la clase Animal
    // Esto es un ejemplo de polimorfismo: cada subclase implementa este método de forma distinta
    @Override
    public void hacerSonido() {
        // Imprime en consola el sonido característico de la vaca, junto con su nombre
        System.out.println(getNombre() + " dice: muuuuu!");
    }
}