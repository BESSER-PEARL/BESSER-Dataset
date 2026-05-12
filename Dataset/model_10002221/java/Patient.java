





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String prenomPatien;
    private String lieuResidence;
    private String profession;
    private int agePatient;
    private int numeroPatien;
    private String nomPatient;





    private List<DossierPatient> dossierpatients;


    public Patient(
        String prenomPatien,        String lieuResidence,        String profession,        int agePatient,        int numeroPatien,        String nomPatient    ) {
        this.prenomPatien = prenomPatien;
        this.lieuResidence = lieuResidence;
        this.profession = profession;
        this.agePatient = agePatient;
        this.numeroPatien = numeroPatien;
        this.nomPatient = nomPatient;
        this.dossierpatients = new ArrayList<>();
    }

    public Patient(
        String prenomPatien,        String lieuResidence,        String profession,        int agePatient,        int numeroPatien,        String nomPatient        ArrayList<DossierPatient> dossierpatients    ) {
        this.prenomPatien = prenomPatien;
        this.lieuResidence = lieuResidence;
        this.profession = profession;
        this.agePatient = agePatient;
        this.numeroPatien = numeroPatien;
        this.nomPatient = nomPatient;
        this.dossierpatients = dossierpatients;
    }

    public String getPrenompatien() {
        return prenomPatien;
    }

    public void setPrenompatien(String prenomPatien) {
        this.prenomPatien = prenomPatien;
    }
    public String getLieuresidence() {
        return lieuResidence;
    }

    public void setLieuresidence(String lieuResidence) {
        this.lieuResidence = lieuResidence;
    }
    public String getProfession() {
        return profession;
    }

    public void setProfession(String profession) {
        this.profession = profession;
    }
    public int getAgepatient() {
        return agePatient;
    }

    public void setAgepatient(int agePatient) {
        this.agePatient = agePatient;
    }
    public int getNumeropatien() {
        return numeroPatien;
    }

    public void setNumeropatien(int numeroPatien) {
        this.numeroPatien = numeroPatien;
    }
    public String getNompatient() {
        return nomPatient;
    }

    public void setNompatient(String nomPatient) {
        this.nomPatient = nomPatient;
    }

    public List<DossierPatient> getDossierpatients() {
        return dossierpatients;
    }

    public void addDossierpatient(Dossierpatient dossierpatient) {
        this.dossierpatients.add(dossierpatient);
    }

}