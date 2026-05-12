





import java.util.List;
import java.util.ArrayList;

public class Gato  {

    private String color;
    private String raza;
    private String nombre;



    public Gato(
        String color,        String raza,        String nombre    ) {
        this.color = color;
        this.raza = raza;
        this.nombre = nombre;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
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


}