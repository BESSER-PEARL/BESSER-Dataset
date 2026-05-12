





import java.util.List;
import java.util.ArrayList;

public class Libros  {

    private String n_meroP_ginas;





    private List<Documentos> documentoss;


    public Libros(
        String n_meroP_ginas    ) {
        this.n_meroP_ginas = n_meroP_ginas;
        this.documentoss = new ArrayList<>();
    }

    public Libros(
        String n_meroP_ginas        ArrayList<Documentos> documentoss    ) {
        this.n_meroP_ginas = n_meroP_ginas;
        this.documentoss = documentoss;
    }

    public String getN_merop_ginas() {
        return n_meroP_ginas;
    }

    public void setN_merop_ginas(String n_meroP_ginas) {
        this.n_meroP_ginas = n_meroP_ginas;
    }

    public List<Documentos> getDocumentoss() {
        return documentoss;
    }

    public void addDocumentos(Documentos documentos) {
        this.documentoss.add(documentos);
    }

}