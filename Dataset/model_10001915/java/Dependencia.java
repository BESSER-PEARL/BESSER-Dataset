





import java.util.List;
import java.util.ArrayList;

public class Dependencia  {

    private String codigo;
    private String responsable;
    private String nombre;





    private SolicitudSuministro solicitudsuministro;


    public Dependencia(
        String codigo,        String responsable,        String nombre    ) {
        this.codigo = codigo;
        this.responsable = responsable;
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
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public SolicitudSuministro getSolicitudsuministro() {
        return solicitudsuministro;
    }

    public void setSolicitudsuministro(SolicitudSuministro solicitudsuministro) {
        this.solicitudsuministro = solicitudsuministro;
    }

}