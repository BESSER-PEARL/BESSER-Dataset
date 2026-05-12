





import java.util.List;
import java.util.ArrayList;

public class ResultatExamen  {

    private int numeroResultat;
    private String infoResultat;





    private Patient patient;




    private Medecin medecin;


    public ResultatExamen(
        int numeroResultat,        String infoResultat    ) {
        this.numeroResultat = numeroResultat;
        this.infoResultat = infoResultat;
    }


    public int getNumeroresultat() {
        return numeroResultat;
    }

    public void setNumeroresultat(int numeroResultat) {
        this.numeroResultat = numeroResultat;
    }
    public String getInforesultat() {
        return infoResultat;
    }

    public void setInforesultat(String infoResultat) {
        this.infoResultat = infoResultat;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }
    public Medecin getMedecin() {
        return medecin;
    }

    public void setMedecin(Medecin medecin) {
        this.medecin = medecin;
    }

}