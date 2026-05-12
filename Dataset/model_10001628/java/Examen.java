





import java.util.List;
import java.util.ArrayList;

public class Examen  {

    private String dateProvisoir;
    private String motif;
    private int numeroExamen;
    private String heure;



    public Examen(
        String dateProvisoir,        String motif,        int numeroExamen,        String heure    ) {
        this.dateProvisoir = dateProvisoir;
        this.motif = motif;
        this.numeroExamen = numeroExamen;
        this.heure = heure;
    }


    public String getDateprovisoir() {
        return dateProvisoir;
    }

    public void setDateprovisoir(String dateProvisoir) {
        this.dateProvisoir = dateProvisoir;
    }
    public String getMotif() {
        return motif;
    }

    public void setMotif(String motif) {
        this.motif = motif;
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


}