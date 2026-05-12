





import java.util.List;
import java.util.ArrayList;

public class Dependencia  {

    private String Codigo;
    private String Nombre;
    private String Responsable;





    private List<Solicitud_suministro> solicitud_suministros;


    public Dependencia(
        String Codigo,        String Nombre,        String Responsable    ) {
        this.Codigo = Codigo;
        this.Nombre = Nombre;
        this.Responsable = Responsable;
        this.solicitud_suministros = new ArrayList<>();
    }

    public Dependencia(
        String Codigo,        String Nombre,        String Responsable        ArrayList<Solicitud_suministro> solicitud_suministros    ) {
        this.Codigo = Codigo;
        this.Nombre = Nombre;
        this.Responsable = Responsable;
        this.solicitud_suministros = solicitud_suministros;
    }

    public String getCodigo() {
        return Codigo;
    }

    public void setCodigo(String Codigo) {
        this.Codigo = Codigo;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getResponsable() {
        return Responsable;
    }

    public void setResponsable(String Responsable) {
        this.Responsable = Responsable;
    }

    public List<Solicitud_suministro> getSolicitud_suministros() {
        return solicitud_suministros;
    }

    public void addSolicitud_suministro(Solicitud_suministro solicitud_suministro) {
        this.solicitud_suministros.add(solicitud_suministro);
    }

}