





import java.util.List;
import java.util.ArrayList;

public class Programme  {

    private String heure;
    private String date;
    private String numeroProgramme;





    private Medecin medecin;


    public Programme(
        String heure,        String date,        String numeroProgramme    ) {
        this.heure = heure;
        this.date = date;
        this.numeroProgramme = numeroProgramme;
    }


    public String getHeure() {
        return heure;
    }

    public void setHeure(String heure) {
        this.heure = heure;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getNumeroprogramme() {
        return numeroProgramme;
    }

    public void setNumeroprogramme(String numeroProgramme) {
        this.numeroProgramme = numeroProgramme;
    }

    public Medecin getMedecin() {
        return medecin;
    }

    public void setMedecin(Medecin medecin) {
        this.medecin = medecin;
    }

}