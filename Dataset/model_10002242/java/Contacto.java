





import java.util.List;
import java.util.ArrayList;

public class Contacto  {

    private String email;
    private String nombre;





    private Libro_de_Direcciones libro_de_direcciones;


    public Contacto(
        String email,        String nombre    ) {
        this.email = email;
        this.nombre = nombre;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public Libro_de_Direcciones getLibro_de_direcciones() {
        return libro_de_direcciones;
    }

    public void setLibro_de_direcciones(Libro_de_Direcciones libro_de_direcciones) {
        this.libro_de_direcciones = libro_de_direcciones;
    }

}