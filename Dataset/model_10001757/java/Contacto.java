





import java.util.List;
import java.util.ArrayList;

public class Contacto  {

    private String Nombre;
    private String Correo;





    private Directorio directorio;


    public Contacto(
        String Nombre,        String Correo    ) {
        this.Nombre = Nombre;
        this.Correo = Correo;
    }


    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getCorreo() {
        return Correo;
    }

    public void setCorreo(String Correo) {
        this.Correo = Correo;
    }

    public Directorio getDirectorio() {
        return directorio;
    }

    public void setDirectorio(Directorio directorio) {
        this.directorio = directorio;
    }

}