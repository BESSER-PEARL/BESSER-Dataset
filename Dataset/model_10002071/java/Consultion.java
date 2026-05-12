





import java.util.List;
import java.util.ArrayList;

public class Consultion  {

    private String description;
    private int numeroConsultation;
    private String dateConsultation;
    private String heure;





    private Rendez_Vous rendez_vous;


    public Consultion(
        String description,        int numeroConsultation,        String dateConsultation,        String heure    ) {
        this.description = description;
        this.numeroConsultation = numeroConsultation;
        this.dateConsultation = dateConsultation;
        this.heure = heure;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getNumeroconsultation() {
        return numeroConsultation;
    }

    public void setNumeroconsultation(int numeroConsultation) {
        this.numeroConsultation = numeroConsultation;
    }
    public String getDateconsultation() {
        return dateConsultation;
    }

    public void setDateconsultation(String dateConsultation) {
        this.dateConsultation = dateConsultation;
    }
    public String getHeure() {
        return heure;
    }

    public void setHeure(String heure) {
        this.heure = heure;
    }

    public Rendez_Vous getRendez_vous() {
        return rendez_vous;
    }

    public void setRendez_vous(Rendez_Vous rendez_vous) {
        this.rendez_vous = rendez_vous;
    }

}