





import java.util.List;
import java.util.ArrayList;

public class HAL_ArtOuvrageType extends ReferenceBiblioType {

    private String edsci;
    private String edcom;
    private String urldoi;
    private String serie;
    private String titouv;
    private String annee;



    public HAL_ArtOuvrageType(
        String edsci,        String edcom,        String urldoi,        String serie,        String titouv,        String annee    ) {
        super(
        );
        this.edsci = edsci;
        this.edcom = edcom;
        this.urldoi = urldoi;
        this.serie = serie;
        this.titouv = titouv;
        this.annee = annee;
    }


    public String getEdsci() {
        return edsci;
    }

    public void setEdsci(String edsci) {
        this.edsci = edsci;
    }
    public String getEdcom() {
        return edcom;
    }

    public void setEdcom(String edcom) {
        this.edcom = edcom;
    }
    public String getUrldoi() {
        return urldoi;
    }

    public void setUrldoi(String urldoi) {
        this.urldoi = urldoi;
    }
    public String getSerie() {
        return serie;
    }

    public void setSerie(String serie) {
        this.serie = serie;
    }
    public String getTitouv() {
        return titouv;
    }

    public void setTitouv(String titouv) {
        this.titouv = titouv;
    }
    public String getAnnee() {
        return annee;
    }

    public void setAnnee(String annee) {
        this.annee = annee;
    }


}