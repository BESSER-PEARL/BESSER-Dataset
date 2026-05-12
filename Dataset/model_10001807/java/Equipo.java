





import java.util.List;
import java.util.ArrayList;

public class Equipo  {

    private String nombre;





    private Partido partido;


    public Equipo(
        String nombre    ) {
        this.nombre = nombre;
    }


    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public Partido getPartido() {
        return partido;
    }

    public void setPartido(Partido partido) {
        this.partido = partido;
    }

}