





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int agePatient;
    private String lieuResidence;
    private String profession;
    private String prenomPatien;
    private String nomPatient;
    private int numeroPatien;





    private List<DossierPatient> dossierpatients;


    public Patient(
        int agePatient,        String lieuResidence,        String profession,        String prenomPatien,        String nomPatient,        int numeroPatien    ) {
        this.agePatient = agePatient;
        this.lieuResidence = lieuResidence;
        this.profession = profession;
        this.prenomPatien = prenomPatien;
        this.nomPatient = nomPatient;
        this.numeroPatien = numeroPatien;
        this.dossierpatients = new ArrayList<>();
    }

    public Patient(
        int agePatient,        String lieuResidence,        String profession,        String prenomPatien,        String nomPatient,        int numeroPatien        ArrayList<DossierPatient> dossierpatients    ) {
        this.agePatient = agePatient;
        this.lieuResidence = lieuResidence;
        this.profession = profession;
        this.prenomPatien = prenomPatien;
        this.nomPatient = nomPatient;
        this.numeroPatien = numeroPatien;
        this.dossierpatients = dossierpatients;
    }

    public int getAgepatient() {
        return agePatient;
    }

    public void setAgepatient(int agePatient) {
        this.agePatient = agePatient;
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
    public String getPrenompatien() {
        return prenomPatien;
    }

    public void setPrenompatien(String prenomPatien) {
        this.prenomPatien = prenomPatien;
    }
    public String getNompatient() {
        return nomPatient;
    }

    public void setNompatient(String nomPatient) {
        this.nomPatient = nomPatient;
    }
    public int getNumeropatien() {
        return numeroPatien;
    }

    public void setNumeropatien(int numeroPatien) {
        this.numeroPatien = numeroPatien;
    }

    public List<DossierPatient> getDossierpatients() {
        return dossierpatients;
    }

    public void addDossierpatient(Dossierpatient dossierpatient) {
        this.dossierpatients.add(dossierpatient);
    }

}