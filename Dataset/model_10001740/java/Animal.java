





import java.util.List;
import java.util.ArrayList;

public class Animal  {

    private String identificador;
    private String raza;
    private String nombre;



    public Animal(
        String identificador,        String raza,        String nombre    ) {
        this.identificador = identificador;
        this.raza = raza;
        this.nombre = nombre;
    }


    public String getIdentificador() {
        return identificador;
    }

    public void setIdentificador(String identificador) {
        this.identificador = identificador;
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