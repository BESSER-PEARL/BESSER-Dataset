





import java.util.List;
import java.util.ArrayList;

public class BD_Tabla  {

    private String nombre;





    private BD_EsquemaBD bd_esquemabd;


    public BD_Tabla(
        String nombre    ) {
        this.nombre = nombre;
    }


    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public BD_EsquemaBD getBd_esquemabd() {
        return bd_esquemabd;
    }

    public void setBd_esquemabd(BD_EsquemaBD bd_esquemabd) {
        this.bd_esquemabd = bd_esquemabd;
    }

}