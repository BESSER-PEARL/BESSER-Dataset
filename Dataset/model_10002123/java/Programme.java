





import java.util.List;
import java.util.ArrayList;

public class Programme  {

    private String numeroProgramme;
    private String date;
    private String heure;





    private Examen examen;


    public Programme(
        String numeroProgramme,        String date,        String heure    ) {
        this.numeroProgramme = numeroProgramme;
        this.date = date;
        this.heure = heure;
    }


    public String getNumeroprogramme() {
        return numeroProgramme;
    }

    public void setNumeroprogramme(String numeroProgramme) {
        this.numeroProgramme = numeroProgramme;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
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