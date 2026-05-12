





import java.util.List;
import java.util.ArrayList;

public class DossierPatient  {

    private int heure;
    private String infoAntecedant;
    private int numeroPatient;
    private String nomDossier;
    private int dateCreation;



    public DossierPatient(
        int heure,        String infoAntecedant,        int numeroPatient,        String nomDossier,        int dateCreation    ) {
        this.heure = heure;
        this.infoAntecedant = infoAntecedant;
        this.numeroPatient = numeroPatient;
        this.nomDossier = nomDossier;
        this.dateCreation = dateCreation;
    }


    public int getHeure() {
        return heure;
    }

    public void setHeure(int heure) {
        this.heure = heure;
    }
    public String getInfoantecedant() {
        return infoAntecedant;
    }

    public void setInfoantecedant(String infoAntecedant) {
        this.infoAntecedant = infoAntecedant;
    }
    public int getNumeropatient() {
        return numeroPatient;
    }

    public void setNumeropatient(int numeroPatient) {
        this.numeroPatient = numeroPatient;
    }
    public String getNomdossier() {
        return nomDossier;
    }

    public void setNomdossier(String nomDossier) {
        this.nomDossier = nomDossier;
    }
    public int getDatecreation() {
        return dateCreation;
    }

    public void setDatecreation(int dateCreation) {
        this.dateCreation = dateCreation;
    }


}