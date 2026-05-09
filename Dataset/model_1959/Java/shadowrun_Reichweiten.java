





import java.util.List;
import java.util.ArrayList;

public class shadowrun_Reichweiten  {






    private List<shadowrun_Reichweite> shadowrun_reichweites;


    public shadowrun_Reichweiten(
    ) {
        this.shadowrun_reichweites = new ArrayList<>();
    }

    public shadowrun_Reichweiten(
        ArrayList<shadowrun_Reichweite> shadowrun_reichweites    ) {
        this.shadowrun_reichweites = shadowrun_reichweites;
    }


    public List<shadowrun_Reichweite> getShadowrun_reichweites() {
        return shadowrun_reichweites;
    }

    public void addShadowrun_reichweite(Shadowrun_reichweite shadowrun_reichweite) {
        this.shadowrun_reichweites.add(shadowrun_reichweite);
    }

}