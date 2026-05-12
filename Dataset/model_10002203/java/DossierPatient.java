





import java.util.List;
import java.util.ArrayList;

public class DossierPatient  {

    private int heure;
    private String nomDossier;
    private int numeroPatient;
    private int dateCreation;
    private String infoAntecedant;



    public DossierPatient(
        int heure,        String nomDossier,        int numeroPatient,        int dateCreation,        String infoAntecedant    ) {
        this.heure = heure;
        this.nomDossier = nomDossier;
        this.numeroPatient = numeroPatient;
        this.dateCreation = dateCreation;
        this.infoAntecedant = infoAntecedant;
    }


    public int getHeure() {
        return heure;
    }

    public void setHeure(int heure) {
        this.heure = heure;
    }
    public String getNomdossier() {
        return nomDossier;
    }

    public void setNomdossier(String nomDossier) {
        this.nomDossier = nomDossier;
    }
    public int getNumeropatient() {
        return numeroPatient;
    }

    public void setNumeropatient(int numeroPatient) {
        this.numeroPatient = numeroPatient;
    }
    public int getDatecreation() {
        return dateCreation;
    }

    public void setDatecreation(int dateCreation) {
        this.dateCreation = dateCreation;
    }
    public String getInfoantecedant() {
        return infoAntecedant;
    }

    public void setInfoantecedant(String infoAntecedant) {
        this.infoAntecedant = infoAntecedant;
    }


}