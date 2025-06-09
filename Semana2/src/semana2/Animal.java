/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package semana2;

/**
 *
 * @author SANTI
 */
// Clase abstracta que representa un Animal
public abstract class Animal {
    // Atributos privados (encapsulados): solo accesibles dentro de esta clase
    private String nombre; 
    private int edad;   

    // Constructor que inicializa los atributos nombre y edad del animal
    public Animal(String nombre, int edad) {
        this.nombre = nombre; // Asigna el valor recibido al atributo nombre
        this.edad = edad;      // Asigna el valor recibido al atributo edad
    }

     // Método público que permite obtener el nombre del animal (encapsulación)
    public String getNombre() {
        return nombre; // Devuelve el valor del atributo nombre
    }
    
    // Método público que permite obtener la edad del animal (encapsulación)
    public int getEdad() {
        return edad;    // Devuelve el valor del atributo edad
    }

     // Método abstracto que deberán definir las clases hijas
    // Esto permite el uso de polimorfismo: cada animal puede hacer un sonido distinto
    public abstract void hacerSonido();
}
