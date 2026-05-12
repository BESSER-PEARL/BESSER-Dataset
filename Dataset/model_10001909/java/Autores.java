





import java.util.List;
import java.util.ArrayList;

public class Autores  {

    private String fechaEliminaci_n;
    private String fechamodificaci_n;
    private String fechaCreaci_n;





    private List<Documentos> documentoss;


    public Autores(
        String fechaEliminaci_n,        String fechamodificaci_n,        String fechaCreaci_n    ) {
        this.fechaEliminaci_n = fechaEliminaci_n;
        this.fechamodificaci_n = fechamodificaci_n;
        this.fechaCreaci_n = fechaCreaci_n;
        this.documentoss = new ArrayList<>();
    }

    public Autores(
        String fechaEliminaci_n,        String fechamodificaci_n,        String fechaCreaci_n        ArrayList<Documentos> documentoss    ) {
        this.fechaEliminaci_n = fechaEliminaci_n;
        this.fechamodificaci_n = fechamodificaci_n;
        this.fechaCreaci_n = fechaCreaci_n;
        this.documentoss = documentoss;
    }

    public String getFechaeliminaci_n() {
        return fechaEliminaci_n;
    }

    public void setFechaeliminaci_n(String fechaEliminaci_n) {
        this.fechaEliminaci_n = fechaEliminaci_n;
    }
    public String getFechamodificaci_n() {
        return fechamodificaci_n;
    }

    public void setFechamodificaci_n(String fechamodificaci_n) {
        this.fechamodificaci_n = fechamodificaci_n;
    }
    public String getFechacreaci_n() {
        return fechaCreaci_n;
    }

    public void setFechacreaci_n(String fechaCreaci_n) {
        this.fechaCreaci_n = fechaCreaci_n;
    }

    public List<Documentos> getDocumentoss() {
        return documentoss;
    }

    public void addDocumentos(Documentos documentos) {
        this.documentoss.add(documentos);
    }

}