





import java.util.List;
import java.util.ArrayList;

public class HAL_OuvrageType extends ReferenceBiblioType {

    private String urldoi;
    private String edcom;
    private String annee;
    private String page;



    public HAL_OuvrageType(
        String urldoi,        String edcom,        String annee,        String page    ) {
        super(
        );
        this.urldoi = urldoi;
        this.edcom = edcom;
        this.annee = annee;
        this.page = page;
    }


    public String getUrldoi() {
        return urldoi;
    }

    public void setUrldoi(String urldoi) {
        this.urldoi = urldoi;
    }
    public String getEdcom() {
        return edcom;
    }

    public void setEdcom(String edcom) {
        this.edcom = edcom;
    }
    public String getAnnee() {
        return annee;
    }

    public void setAnnee(String annee) {
        this.annee = annee;
    }
    public String getPage() {
        return page;
    }

    public void setPage(String page) {
        this.page = page;
    }


}