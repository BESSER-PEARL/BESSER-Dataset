





import java.util.List;
import java.util.ArrayList;

public class Dependencia  {

    private String codgio;
    private String nombre;
    private String reponsable;





    private List<SolicitudSuministro> solicitudsuministros;


    public Dependencia(
        String codgio,        String nombre,        String reponsable    ) {
        this.codgio = codgio;
        this.nombre = nombre;
        this.reponsable = reponsable;
        this.solicitudsuministros = new ArrayList<>();
    }

    public Dependencia(
        String codgio,        String nombre,        String reponsable        ArrayList<SolicitudSuministro> solicitudsuministros    ) {
        this.codgio = codgio;
        this.nombre = nombre;
        this.reponsable = reponsable;
        this.solicitudsuministros = solicitudsuministros;
    }

    public String getCodgio() {
        return codgio;
    }

    public void setCodgio(String codgio) {
        this.codgio = codgio;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getReponsable() {
        return reponsable;
    }

    public void setReponsable(String reponsable) {
        this.reponsable = reponsable;
    }

    public List<SolicitudSuministro> getSolicitudsuministros() {
        return solicitudsuministros;
    }

    public void addSolicitudsuministro(Solicitudsuministro solicitudsuministro) {
        this.solicitudsuministros.add(solicitudsuministro);
    }

}