





import java.util.List;
import java.util.ArrayList;

public class Fragmentos_Fichero  {

    private String nombre;





    private Fragmentos_Aplicacion fragmentos_aplicacion;


    public Fragmentos_Fichero(
        String nombre    ) {
        this.nombre = nombre;
    }


    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public Fragmentos_Aplicacion getFragmentos_aplicacion() {
        return fragmentos_aplicacion;
    }

    public void setFragmentos_aplicacion(Fragmentos_Aplicacion fragmentos_aplicacion) {
        this.fragmentos_aplicacion = fragmentos_aplicacion;
    }

}