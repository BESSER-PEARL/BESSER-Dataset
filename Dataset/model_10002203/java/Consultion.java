





import java.util.List;
import java.util.ArrayList;

public class Consultion  {

    private String description;
    private String heure;
    private int numeroConsultation;
    private String dateConsultation;





    private Rendez_Vous rendez_vous;


    public Consultion(
        String description,        String heure,        int numeroConsultation,        String dateConsultation    ) {
        this.description = description;
        this.heure = heure;
        this.numeroConsultation = numeroConsultation;
        this.dateConsultation = dateConsultation;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getHeure() {
        return heure;
    }

    public void setHeure(String heure) {
        this.heure = heure;
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

    public Rendez_Vous getRendez_vous() {
        return rendez_vous;
    }

    public void setRendez_vous(Rendez_Vous rendez_vous) {
        this.rendez_vous = rendez_vous;
    }

}