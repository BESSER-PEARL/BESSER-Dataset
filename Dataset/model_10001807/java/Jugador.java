





import java.util.List;
import java.util.ArrayList;

public class Jugador  {

    private String nombre;
    private String nif;
    private int telefono;
    private String apellidos;





    private Equipo equipo;




    private Fecha fecha;


    public Jugador(
        String nombre,        String nif,        int telefono,        String apellidos    ) {
        this.nombre = nombre;
        this.nif = nif;
        this.telefono = telefono;
        this.apellidos = apellidos;
    }


    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getNif() {
        return nif;
    }

    public void setNif(String nif) {
        this.nif = nif;
    }
    public int getTelefono() {
        return telefono;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }
    public String getApellidos() {
        return apellidos;
    }

    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }

    public Equipo getEquipo() {
        return equipo;
    }

    public void setEquipo(Equipo equipo) {
        this.equipo = equipo;
    }
    public Fecha getFecha() {
        return fecha;
    }

    public void setFecha(Fecha fecha) {
        this.fecha = fecha;
    }

}