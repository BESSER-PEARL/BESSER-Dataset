





import java.util.List;
import java.util.ArrayList;

public class ArticulosCient_ficos  {

    private String SSN;





    private List<Documentos> documentoss;


    public ArticulosCient_ficos(
        String SSN    ) {
        this.SSN = SSN;
        this.documentoss = new ArrayList<>();
    }

    public ArticulosCient_ficos(
        String SSN        ArrayList<Documentos> documentoss    ) {
        this.SSN = SSN;
        this.documentoss = documentoss;
    }

    public String getSsn() {
        return SSN;
    }

    public void setSsn(String SSN) {
        this.SSN = SSN;
    }

    public List<Documentos> getDocumentoss() {
        return documentoss;
    }

    public void addDocumentos(Documentos documentos) {
        this.documentoss.add(documentos);
    }

}