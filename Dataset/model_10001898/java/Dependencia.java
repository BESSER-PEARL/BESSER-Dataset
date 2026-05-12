





import java.util.List;
import java.util.ArrayList;

public class Dependencia  {

    private String nombre;
    private String codigo;
    private String responsable;



    public Dependencia(
        String nombre,        String codigo,        String responsable    ) {
        this.nombre = nombre;
        this.codigo = codigo;
        this.responsable = responsable;
    }


    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }
    public String getResponsable() {
        return responsable;
    }

    public void setResponsable(String responsable) {
        this.responsable = responsable;
    }


}