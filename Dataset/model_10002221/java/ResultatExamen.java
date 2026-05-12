





import java.util.List;
import java.util.ArrayList;

public class ResultatExamen  {

    private String infoResultat;
    private int numeroResultat;





    private Patient patient;




    private Medecin medecin;


    public ResultatExamen(
        String infoResultat,        int numeroResultat    ) {
        this.infoResultat = infoResultat;
        this.numeroResultat = numeroResultat;
    }


    public String getInforesultat() {
        return infoResultat;
    }

    public void setInforesultat(String infoResultat) {
        this.infoResultat = infoResultat;
    }
    public int getNumeroresultat() {
        return numeroResultat;
    }

    public void setNumeroresultat(int numeroResultat) {
        this.numeroResultat = numeroResultat;
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