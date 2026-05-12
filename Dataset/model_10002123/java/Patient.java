





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String nomPatient;
    private int agePatient;
    private String lieuResidence;
    private String prenomPatien;
    private String profession;
    private int numeroPatien;



    public Patient(
        String nomPatient,        int agePatient,        String lieuResidence,        String prenomPatien,        String profession,        int numeroPatien    ) {
        this.nomPatient = nomPatient;
        this.agePatient = agePatient;
        this.lieuResidence = lieuResidence;
        this.prenomPatien = prenomPatien;
        this.profession = profession;
        this.numeroPatien = numeroPatien;
    }


    public String getNompatient() {
        return nomPatient;
    }

    public void setNompatient(String nomPatient) {
        this.nomPatient = nomPatient;
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
    public String getPrenompatien() {
        return prenomPatien;
    }

    public void setPrenompatien(String prenomPatien) {
        this.prenomPatien = prenomPatien;
    }
    public String getProfession() {
        return profession;
    }

    public void setProfession(String profession) {
        this.profession = profession;
    }
    public int getNumeropatien() {
        return numeroPatien;
    }

    public void setNumeropatien(int numeroPatien) {
        this.numeroPatien = numeroPatien;
    }


}