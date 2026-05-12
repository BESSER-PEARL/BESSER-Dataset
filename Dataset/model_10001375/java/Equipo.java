





import java.util.List;
import java.util.ArrayList;

public class Equipo  {

    private String nombre;
    private String registro;





    private Liga liga;


    public Equipo(
        String nombre,        String registro    ) {
        this.nombre = nombre;
        this.registro = registro;
    }


    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getRegistro() {
        return registro;
    }

    public void setRegistro(String registro) {
        this.registro = registro;
    }

    public Liga getLiga() {
        return liga;
    }

    public void setLiga(Liga liga) {
        this.liga = liga;
    }

}