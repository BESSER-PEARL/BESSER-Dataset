





import java.util.List;
import java.util.ArrayList;

public class shadowrun_ModifikatorList  {

    private String name;





    private List<shadowrun_AbstraktModifikatoren> shadowrun_abstraktmodifikatorens;


    public shadowrun_ModifikatorList(
        String name    ) {
        this.name = name;
        this.shadowrun_abstraktmodifikatorens = new ArrayList<>();
    }

    public shadowrun_ModifikatorList(
        String name        ArrayList<shadowrun_AbstraktModifikatoren> shadowrun_abstraktmodifikatorens    ) {
        this.name = name;
        this.shadowrun_abstraktmodifikatorens = shadowrun_abstraktmodifikatorens;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<shadowrun_AbstraktModifikatoren> getShadowrun_abstraktmodifikatorens() {
        return shadowrun_abstraktmodifikatorens;
    }

    public void addShadowrun_abstraktmodifikatoren(Shadowrun_abstraktmodifikatoren shadowrun_abstraktmodifikatoren) {
        this.shadowrun_abstraktmodifikatorens.add(shadowrun_abstraktmodifikatoren);
    }

}