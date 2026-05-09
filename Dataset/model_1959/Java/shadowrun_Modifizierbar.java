





import java.util.List;
import java.util.ArrayList;

public class shadowrun_Modifizierbar  {






    private List<shadowrun_AttributModifikatorWert> shadowrun_attributmodifikatorwerts;




    private shadowrun_AttributModifikatorWert shadowrun_attributmodifikatorwert;


    public shadowrun_Modifizierbar(
    ) {
        this.shadowrun_attributmodifikatorwerts = new ArrayList<>();
    }

    public shadowrun_Modifizierbar(
        ArrayList<shadowrun_AttributModifikatorWert> shadowrun_attributmodifikatorwerts    ) {
        this.shadowrun_attributmodifikatorwerts = shadowrun_attributmodifikatorwerts;
    }


    public List<shadowrun_AttributModifikatorWert> getShadowrun_attributmodifikatorwerts() {
        return shadowrun_attributmodifikatorwerts;
    }

    public void addShadowrun_attributmodifikatorwert(Shadowrun_attributmodifikatorwert shadowrun_attributmodifikatorwert) {
        this.shadowrun_attributmodifikatorwerts.add(shadowrun_attributmodifikatorwert);
    }
    public shadowrun_AttributModifikatorWert getShadowrun_attributmodifikatorwert() {
        return shadowrun_attributmodifikatorwert;
    }

    public void setShadowrun_attributmodifikatorwert(shadowrun_AttributModifikatorWert shadowrun_attributmodifikatorwert) {
        this.shadowrun_attributmodifikatorwert = shadowrun_attributmodifikatorwert;
    }

}