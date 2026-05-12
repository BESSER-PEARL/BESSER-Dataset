





import java.util.List;
import java.util.ArrayList;

public class Liga  {

    private String nombre;
    private String datos_comienzo;
    private String datos_finalizaci_n;



    public Liga(
        String nombre,        String datos_comienzo,        String datos_finalizaci_n    ) {
        this.nombre = nombre;
        this.datos_comienzo = datos_comienzo;
        this.datos_finalizaci_n = datos_finalizaci_n;
    }


    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getDatos_comienzo() {
        return datos_comienzo;
    }

    public void setDatos_comienzo(String datos_comienzo) {
        this.datos_comienzo = datos_comienzo;
    }
    public String getDatos_finalizaci_n() {
        return datos_finalizaci_n;
    }

    public void setDatos_finalizaci_n(String datos_finalizaci_n) {
        this.datos_finalizaci_n = datos_finalizaci_n;
    }


}