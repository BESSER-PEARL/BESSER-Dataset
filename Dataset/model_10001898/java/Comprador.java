





import java.util.List;
import java.util.ArrayList;

public class Comprador  {

    private String Nombre;
    private String telefono;
    private String identificacion;



    public Comprador(
        String Nombre,        String telefono,        String identificacion    ) {
        this.Nombre = Nombre;
        this.telefono = telefono;
        this.identificacion = identificacion;
    }


    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }
    public String getIdentificacion() {
        return identificacion;
    }

    public void setIdentificacion(String identificacion) {
        this.identificacion = identificacion;
    }


}