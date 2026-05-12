





import java.util.List;
import java.util.ArrayList;

public class HAL_WorkshopType extends ReferenceBiblioType {

    private String annee;
    private String urldoi;
    private String titconf;
    private String edcom;
    private String ville;
    private String edsci;
    private String pays;
    private String serie;
    private String page;



    public HAL_WorkshopType(
        String annee,        String urldoi,        String titconf,        String edcom,        String ville,        String edsci,        String pays,        String serie,        String page    ) {
        super(
        );
        this.annee = annee;
        this.urldoi = urldoi;
        this.titconf = titconf;
        this.edcom = edcom;
        this.ville = ville;
        this.edsci = edsci;
        this.pays = pays;
        this.serie = serie;
        this.page = page;
    }


    public String getAnnee() {
        return annee;
    }

    public void setAnnee(String annee) {
        this.annee = annee;
    }
    public String getUrldoi() {
        return urldoi;
    }

    public void setUrldoi(String urldoi) {
        this.urldoi = urldoi;
    }
    public String getTitconf() {
        return titconf;
    }

    public void setTitconf(String titconf) {
        this.titconf = titconf;
    }
    public String getEdcom() {
        return edcom;
    }

    public void setEdcom(String edcom) {
        this.edcom = edcom;
    }
    public String getVille() {
        return ville;
    }

    public void setVille(String ville) {
        this.ville = ville;
    }
    public String getEdsci() {
        return edsci;
    }

    public void setEdsci(String edsci) {
        this.edsci = edsci;
    }
    public String getPays() {
        return pays;
    }

    public void setPays(String pays) {
        this.pays = pays;
    }
    public String getSerie() {
        return serie;
    }

    public void setSerie(String serie) {
        this.serie = serie;
    }
    public String getPage() {
        return page;
    }

    public void setPage(String page) {
        this.page = page;
    }


}