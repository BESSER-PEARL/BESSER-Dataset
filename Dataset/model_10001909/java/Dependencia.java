





import java.util.List;
import java.util.ArrayList;

public class Dependencia  {

    private String codigo;
    private String responsable;
    private String nombre;





    private List<SolicitudSuministro> solicitudsuministros;


    public Dependencia(
        String codigo,        String responsable,        String nombre    ) {
        this.codigo = codigo;
        this.responsable = responsable;
        this.nombre = nombre;
        this.solicitudsuministros = new ArrayList<>();
    }

    public Dependencia(
        String codigo,        String responsable,        String nombre        ArrayList<SolicitudSuministro> solicitudsuministros    ) {
        this.codigo = codigo;
        this.responsable = responsable;
        this.nombre = nombre;
        this.solicitudsuministros = solicitudsuministros;
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

    public List<SolicitudSuministro> getSolicitudsuministros() {
        return solicitudsuministros;
    }

    public void addSolicitudsuministro(Solicitudsuministro solicitudsuministro) {
        this.solicitudsuministros.add(solicitudsuministro);
    }

}