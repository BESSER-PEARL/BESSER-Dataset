





import java.util.List;
import java.util.ArrayList;

public class Programme  {

    private String date;
    private String numeroProgramme;
    private String heure;





    private Examen examen;


    public Programme(
        String date,        String numeroProgramme,        String heure    ) {
        this.date = date;
        this.numeroProgramme = numeroProgramme;
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
    public String getHeure() {
        return heure;
    }

    public void setHeure(String heure) {
        this.heure = heure;
    }

    public Examen getExamen() {
        return examen;
    }

    public void setExamen(Examen examen) {
        this.examen = examen;
    }

}