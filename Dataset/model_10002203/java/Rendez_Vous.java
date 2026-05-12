





import java.util.List;
import java.util.ArrayList;

public class Rendez_Vous  {

    private String lieuRDV;
    private String dateRDV;
    private String heure;
    private int numeroRdV;





    private Patient patient;


    public Rendez_Vous(
        String lieuRDV,        String dateRDV,        String heure,        int numeroRdV    ) {
        this.lieuRDV = lieuRDV;
        this.dateRDV = dateRDV;
        this.heure = heure;
        this.numeroRdV = numeroRdV;
    }


    public String getLieurdv() {
        return lieuRDV;
    }

    public void setLieurdv(String lieuRDV) {
        this.lieuRDV = lieuRDV;
    }
    public String getDaterdv() {
        return dateRDV;
    }

    public void setDaterdv(String dateRDV) {
        this.dateRDV = dateRDV;
    }
    public String getHeure() {
        return heure;
    }

    public void setHeure(String heure) {
        this.heure = heure;
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