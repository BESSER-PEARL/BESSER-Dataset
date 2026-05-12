





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String allergies;
    private String antecedent;
    private String traitement;





    private List<RDV> rdvs;




    private Medecin medecin;


    public Patient(
        String allergies,        String antecedent,        String traitement    ) {
        this.allergies = allergies;
        this.antecedent = antecedent;
        this.traitement = traitement;
        this.rdvs = new ArrayList<>();
    }

    public Patient(
        String allergies,        String antecedent,        String traitement        ArrayList<RDV> rdvs    ) {
        this.allergies = allergies;
        this.antecedent = antecedent;
        this.traitement = traitement;
        this.rdvs = rdvs;
    }

    public String getAllergies() {
        return allergies;
    }

    public void setAllergies(String allergies) {
        this.allergies = allergies;
    }
    public String getAntecedent() {
        return antecedent;
    }

    public void setAntecedent(String antecedent) {
        this.antecedent = antecedent;
    }
    public String getTraitement() {
        return traitement;
    }

    public void setTraitement(String traitement) {
        this.traitement = traitement;
    }

    public List<RDV> getRdvs() {
        return rdvs;
    }

    public void addRdv(Rdv rdv) {
        this.rdvs.add(rdv);
    }
    public Medecin getMedecin() {
        return medecin;
    }

    public void setMedecin(Medecin medecin) {
        this.medecin = medecin;
    }

}