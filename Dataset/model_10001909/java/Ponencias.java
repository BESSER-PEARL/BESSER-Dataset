





import java.util.List;
import java.util.ArrayList;

public class Ponencias  {

    private String nombreCongreso;





    private List<Documentos> documentoss;


    public Ponencias(
        String nombreCongreso    ) {
        this.nombreCongreso = nombreCongreso;
        this.documentoss = new ArrayList<>();
    }

    public Ponencias(
        String nombreCongreso        ArrayList<Documentos> documentoss    ) {
        this.nombreCongreso = nombreCongreso;
        this.documentoss = documentoss;
    }

    public String getNombrecongreso() {
        return nombreCongreso;
    }

    public void setNombrecongreso(String nombreCongreso) {
        this.nombreCongreso = nombreCongreso;
    }

    public List<Documentos> getDocumentoss() {
        return documentoss;
    }

    public void addDocumentos(Documentos documentos) {
        this.documentoss.add(documentos);
    }

}