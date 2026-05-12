





import java.util.List;
import java.util.ArrayList;

public class HAL_ArtRevueType extends ReferenceBiblioType {

    private String annee;
    private String urldoi;
    private String page;
    private String volume;
    private String journal;



    public HAL_ArtRevueType(
        String annee,        String urldoi,        String page,        String volume,        String journal    ) {
        super(
        );
        this.annee = annee;
        this.urldoi = urldoi;
        this.page = page;
        this.volume = volume;
        this.journal = journal;
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
    public String getPage() {
        return page;
    }

    public void setPage(String page) {
        this.page = page;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }
    public String getJournal() {
        return journal;
    }

    public void setJournal(String journal) {
        this.journal = journal;
    }


}