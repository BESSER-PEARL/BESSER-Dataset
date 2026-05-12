





import java.util.List;
import java.util.ArrayList;

public class Examen  {

    private String dateProvisoir;
    private int numeroExamen;
    private String heure;
    private String motif;



    public Examen(
        String dateProvisoir,        int numeroExamen,        String heure,        String motif    ) {
        this.dateProvisoir = dateProvisoir;
        this.numeroExamen = numeroExamen;
        this.heure = heure;
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


}