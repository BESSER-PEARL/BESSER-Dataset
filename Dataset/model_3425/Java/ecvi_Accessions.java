





import java.util.List;
import java.util.ArrayList;

public class ecvi_Accessions  {






    private List<ecvi_Accession> ecvi_accessions;


    public ecvi_Accessions(
    ) {
        this.ecvi_accessions = new ArrayList<>();
    }

    public ecvi_Accessions(
        ArrayList<ecvi_Accession> ecvi_accessions    ) {
        this.ecvi_accessions = ecvi_accessions;
    }


    public List<ecvi_Accession> getEcvi_accessions() {
        return ecvi_accessions;
    }

    public void addEcvi_accession(Ecvi_accession ecvi_accession) {
        this.ecvi_accessions.add(ecvi_accession);
    }

}