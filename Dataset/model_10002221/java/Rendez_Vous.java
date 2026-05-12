





import java.util.List;
import java.util.ArrayList;

public class Rendez_Vous  {

    private String heure;
    private String dateRDV;
    private String lieuRDV;
    private int numeroRdV;





    private Patient patient;


    public Rendez_Vous(
        String heure,        String dateRDV,        String lieuRDV,        int numeroRdV    ) {
        this.heure = heure;
        this.dateRDV = dateRDV;
        this.lieuRDV = lieuRDV;
        this.numeroRdV = numeroRdV;
    }


    public String getHeure() {
        return heure;
    }

    public void setHeure(String heure) {
        this.heure = heure;
    }
    public String getDaterdv() {
        return dateRDV;
    }

    public void setDaterdv(String dateRDV) {
        this.dateRDV = dateRDV;
    }
    public String getLieurdv() {
        return lieuRDV;
    }

    public void setLieurdv(String lieuRDV) {
        this.lieuRDV = lieuRDV;
    }
    public int getNumerordv() {
        return numeroRdV;
    }

    public void setNumerordv(int numeroRdV) {
        this.numeroRdV = numeroRdV;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}