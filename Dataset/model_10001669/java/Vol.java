





import java.util.List;
import java.util.ArrayList;

public class Vol  {

    private String dateHeureDepart;
    private String numeroVol;
    private String dateHeureArrivee;
    private None etatVol;



    public Vol(
        String dateHeureDepart,        String numeroVol,        String dateHeureArrivee,        None etatVol    ) {
        this.dateHeureDepart = dateHeureDepart;
        this.numeroVol = numeroVol;
        this.dateHeureArrivee = dateHeureArrivee;
        this.etatVol = etatVol;
    }


    public String getDateheuredepart() {
        return dateHeureDepart;
    }

    public void setDateheuredepart(String dateHeureDepart) {
        this.dateHeureDepart = dateHeureDepart;
    }
    public String getNumerovol() {
        return numeroVol;
    }

    public void setNumerovol(String numeroVol) {
        this.numeroVol = numeroVol;
    }
    public String getDateheurearrivee() {
        return dateHeureArrivee;
    }

    public void setDateheurearrivee(String dateHeureArrivee) {
        this.dateHeureArrivee = dateHeureArrivee;
    }
    public None getEtatvol() {
        return etatVol;
    }

    public void setEtatvol(None etatVol) {
        this.etatVol = etatVol;
    }


}