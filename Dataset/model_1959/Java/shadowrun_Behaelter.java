





import java.util.List;
import java.util.ArrayList;

public class shadowrun_Behaelter extends Gegenstand {

    private int kapazitaet;





    private List<shadowrun_AbstaktGegenstand> shadowrun_abstaktgegenstands;


    public shadowrun_Behaelter(
        int kapazitaet    ) {
        super(
        );
        this.kapazitaet = kapazitaet;
        this.shadowrun_abstaktgegenstands = new ArrayList<>();
    }

    public shadowrun_Behaelter(
        int kapazitaet        ArrayList<shadowrun_AbstaktGegenstand> shadowrun_abstaktgegenstands    ) {
        this.kapazitaet = kapazitaet;
        this.shadowrun_abstaktgegenstands = shadowrun_abstaktgegenstands;
    }

    public int getKapazitaet() {
        return kapazitaet;
    }

    public void setKapazitaet(int kapazitaet) {
        this.kapazitaet = kapazitaet;
    }

    public List<shadowrun_AbstaktGegenstand> getShadowrun_abstaktgegenstands() {
        return shadowrun_abstaktgegenstands;
    }

    public void addShadowrun_abstaktgegenstand(Shadowrun_abstaktgegenstand shadowrun_abstaktgegenstand) {
        this.shadowrun_abstaktgegenstands.add(shadowrun_abstaktgegenstand);
    }

}