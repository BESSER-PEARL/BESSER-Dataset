





import java.util.List;
import java.util.ArrayList;

public class Examen  {

    private String heure;
    private String motif;
    private String dateProvisoir;
    private int numeroExamen;





    private Rendez_Vous rendez_vous;


    public Examen(
        String heure,        String motif,        String dateProvisoir,        int numeroExamen    ) {
        this.heure = heure;
        this.motif = motif;
        this.dateProvisoir = dateProvisoir;
        this.numeroExamen = numeroExamen;
    }


    public String getHeure() {
        return heure;
    }

    public void setHeure(String heure) {
        this.heure = heure;
    }
    public String getMotif() {
        return motif;
    }

    public void setMotif(String motif) {
        this.motif = motif;
    }
    public String getDateprovisoir() {
        return dateProvisoir;
    }

    public void setDateprovisoir(String dateProvisoir) {
        this.dateProvisoir = dateProvisoir;
    }
    public int getNumeroexamen() {
        return numeroExamen;
    }

    public void setNumeroexamen(int numeroExamen) {
        this.numeroExamen = numeroExamen;
    }

    public Rendez_Vous getRendez_vous() {
        return rendez_vous;
    }

    public void setRendez_vous(Rendez_Vous rendez_vous) {
        this.rendez_vous = rendez_vous;
    }

}