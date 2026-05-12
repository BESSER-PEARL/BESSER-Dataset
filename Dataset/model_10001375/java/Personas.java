





import java.util.List;
import java.util.ArrayList;

public class Personas  {

    private String Direccion;
    private String Nombre;



    public Personas(
        String Direccion,        String Nombre    ) {
        this.Direccion = Direccion;
        this.Nombre = Nombre;
    }


    public String getDireccion() {
        return Direccion;
    }

    public void setDireccion(String Direccion) {
        this.Direccion = Direccion;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }


}