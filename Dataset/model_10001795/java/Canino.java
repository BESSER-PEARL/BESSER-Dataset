





import java.util.List;
import java.util.ArrayList;

public class Canino  {

    private None edad;
    private None peso;
    private None altura;
    private String raza;
    private String nombre;
    private String observaciones;



    public Canino(
        None edad,        None peso,        None altura,        String raza,        String nombre,        String observaciones    ) {
        this.edad = edad;
        this.peso = peso;
        this.altura = altura;
        this.raza = raza;
        this.nombre = nombre;
        this.observaciones = observaciones;
    }


    public None getEdad() {
        return edad;
    }

    public void setEdad(None edad) {
        this.edad = edad;
    }
    public None getPeso() {
        return peso;
    }

    public void setPeso(None peso) {
        this.peso = peso;
    }
    public None getAltura() {
        return altura;
    }

    public void setAltura(None altura) {
        this.altura = altura;
    }
    public String getRaza() {
        return raza;
    }

    public void setRaza(String raza) {
        this.raza = raza;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getObservaciones() {
        return observaciones;
    }

    public void setObservaciones(String observaciones) {
        this.observaciones = observaciones;
    }


}