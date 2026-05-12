





import java.util.List;
import java.util.ArrayList;

public class ResultatExamen  {

    private String infoResultat;
    private int numeroResultat;





    private Examen examen;


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

    public Examen getExamen() {
        return examen;
    }

    public void setExamen(Examen examen) {
        this.examen = examen;
    }

}