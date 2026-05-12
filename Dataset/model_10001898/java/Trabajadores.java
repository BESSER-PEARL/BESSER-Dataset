





import java.util.List;
import java.util.ArrayList;

public class Trabajadores  {

    private String nombre;
    private String identificacion;
    private int Telefono;





    private Obras obras;


    public Trabajadores(
        String nombre,        String identificacion,        int Telefono    ) {
        this.nombre = nombre;
        this.identificacion = identificacion;
        this.Telefono = Telefono;
    }


    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getIdentificacion() {
        return identificacion;
    }

    public void setIdentificacion(String identificacion) {
        this.identificacion = identificacion;
    }
    public int getTelefono() {
        return Telefono;
    }

    public void setTelefono(int Telefono) {
        this.Telefono = Telefono;
    }

    public Obras getObras() {
        return obras;
    }

    public void setObras(Obras obras) {
        this.obras = obras;
    }

}