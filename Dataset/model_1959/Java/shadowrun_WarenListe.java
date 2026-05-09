





import java.util.List;
import java.util.ArrayList;

public class shadowrun_WarenListe  {

    private String listenWert;
    private String strassenWert;





    private List<shadowrun_AbstaktGegenstand> shadowrun_abstaktgegenstands;


    public shadowrun_WarenListe(
        String listenWert,        String strassenWert    ) {
        this.listenWert = listenWert;
        this.strassenWert = strassenWert;
        this.shadowrun_abstaktgegenstands = new ArrayList<>();
    }

    public shadowrun_WarenListe(
        String listenWert,        String strassenWert        ArrayList<shadowrun_AbstaktGegenstand> shadowrun_abstaktgegenstands    ) {
        this.listenWert = listenWert;
        this.strassenWert = strassenWert;
        this.shadowrun_abstaktgegenstands = shadowrun_abstaktgegenstands;
    }

    public String getListenwert() {
        return listenWert;
    }

    public void setListenwert(String listenWert) {
        this.listenWert = listenWert;
    }
    public String getStrassenwert() {
        return strassenWert;
    }

    public void setStrassenwert(String strassenWert) {
        this.strassenWert = strassenWert;
    }

    public List<shadowrun_AbstaktGegenstand> getShadowrun_abstaktgegenstands() {
        return shadowrun_abstaktgegenstands;
    }

    public void addShadowrun_abstaktgegenstand(Shadowrun_abstaktgegenstand shadowrun_abstaktgegenstand) {
        this.shadowrun_abstaktgegenstands.add(shadowrun_abstaktgegenstand);
    }

}