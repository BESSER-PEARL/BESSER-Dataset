





import java.util.List;
import java.util.ArrayList;

public class shadowrun_GengenstandListe  {






    private List<shadowrun_AbstaktGegenstand> shadowrun_abstaktgegenstands;


    public shadowrun_GengenstandListe(
    ) {
        this.shadowrun_abstaktgegenstands = new ArrayList<>();
    }

    public shadowrun_GengenstandListe(
        ArrayList<shadowrun_AbstaktGegenstand> shadowrun_abstaktgegenstands    ) {
        this.shadowrun_abstaktgegenstands = shadowrun_abstaktgegenstands;
    }


    public List<shadowrun_AbstaktGegenstand> getShadowrun_abstaktgegenstands() {
        return shadowrun_abstaktgegenstands;
    }

    public void addShadowrun_abstaktgegenstand(Shadowrun_abstaktgegenstand shadowrun_abstaktgegenstand) {
        this.shadowrun_abstaktgegenstands.add(shadowrun_abstaktgegenstand);
    }

}