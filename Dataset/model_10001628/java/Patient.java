





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String nomPatient;
    private String profession;
    private String lieuResidence;
    private String prenomPatien;
    private int agePatient;
    private int numeroPatien;



    public Patient(
        String nomPatient,        String profession,        String lieuResidence,        String prenomPatien,        int agePatient,        int numeroPatien    ) {
        this.nomPatient = nomPatient;
        this.profession = profession;
        this.lieuResidence = lieuResidence;
        this.prenomPatien = prenomPatien;
        this.agePatient = agePatient;
        this.numeroPatien = numeroPatien;
    }


    public String getNompatient() {
        return nomPatient;
    }

    public void setNompatient(String nomPatient) {
        this.nomPatient = nomPatient;
    }
    public String getProfession() {
        return profession;
    }

    public void setProfession(String profession) {
        this.profession = profession;
    }
    public String getLieuresidence() {
        return lieuResidence;
    }

    public void setLieuresidence(String lieuResidence) {
        this.lieuResidence = lieuResidence;
    }
    public String getPrenompatien() {
        return prenomPatien;
    }

    public void setPrenompatien(String prenomPatien) {
        this.prenomPatien = prenomPatien;
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


}