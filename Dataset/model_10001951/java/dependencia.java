





import java.util.List;
import java.util.ArrayList;

public class dependencia  {

    private String codigo;
    private String responsable;
    private String nombre;





    private List<SolicitudSuministros> solicitudsuministross;


    public dependencia(
        String codigo,        String responsable,        String nombre    ) {
        this.codigo = codigo;
        this.responsable = responsable;
        this.nombre = nombre;
        this.solicitudsuministross = new ArrayList<>();
    }

    public dependencia(
        String codigo,        String responsable,        String nombre        ArrayList<SolicitudSuministros> solicitudsuministross    ) {
        this.codigo = codigo;
        this.responsable = responsable;
        this.nombre = nombre;
        this.solicitudsuministross = solicitudsuministross;
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

    public List<SolicitudSuministros> getSolicitudsuministross() {
        return solicitudsuministross;
    }

    public void addSolicitudsuministros(Solicitudsuministros solicitudsuministros) {
        this.solicitudsuministross.add(solicitudsuministros);
    }

}