





import java.util.List;
import java.util.ArrayList;

public class BD_Columna  {

    private String tipo;
    private String nombre;





    private BD_Tabla bd_tabla;


    public BD_Columna(
        String tipo,        String nombre    ) {
        this.tipo = tipo;
        this.nombre = nombre;
    }


    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public BD_Tabla getBd_tabla() {
        return bd_tabla;
    }

    public void setBd_tabla(BD_Tabla bd_tabla) {
        this.bd_tabla = bd_tabla;
    }

}