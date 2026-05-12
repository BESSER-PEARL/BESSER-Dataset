





import java.util.List;
import java.util.ArrayList;

public class Rendez_Vous  {

    private int numeroRdV;
    private String lieuRDV;
    private String heure;
    private String dateRDV;





    private Patient patient;


    public Rendez_Vous(
        int numeroRdV,        String lieuRDV,        String heure,        String dateRDV    ) {
        this.numeroRdV = numeroRdV;
        this.lieuRDV = lieuRDV;
        this.heure = heure;
        this.dateRDV = dateRDV;
    }


    public int getNumerordv() {
        return numeroRdV;
    }

    public void setNumerordv(int numeroRdV) {
        this.numeroRdV = numeroRdV;
    }
    public String getLieurdv() {
        return lieuRDV;
    }

    public void setLieurdv(String lieuRDV) {
        this.lieuRDV = lieuRDV;
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

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}