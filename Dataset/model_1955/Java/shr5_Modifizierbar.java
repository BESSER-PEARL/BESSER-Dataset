





import java.util.List;
import java.util.ArrayList;

public class shr5_Modifizierbar  {






    private shr5_AttributModifikatorWert shr5_attributmodifikatorwert;




    private List<shr5_AttributModifikatorWert> shr5_attributmodifikatorwerts;


    public shr5_Modifizierbar(
    ) {
        this.shr5_attributmodifikatorwerts = new ArrayList<>();
    }

    public shr5_Modifizierbar(
        ArrayList<shr5_AttributModifikatorWert> shr5_attributmodifikatorwerts    ) {
        this.shr5_attributmodifikatorwerts = shr5_attributmodifikatorwerts;
    }


    public shr5_AttributModifikatorWert getShr5_attributmodifikatorwert() {
        return shr5_attributmodifikatorwert;
    }

    public void setShr5_attributmodifikatorwert(shr5_AttributModifikatorWert shr5_attributmodifikatorwert) {
        this.shr5_attributmodifikatorwert = shr5_attributmodifikatorwert;
    }
    public List<shr5_AttributModifikatorWert> getShr5_attributmodifikatorwerts() {
        return shr5_attributmodifikatorwerts;
    }

    public void addShr5_attributmodifikatorwert(Shr5_attributmodifikatorwert shr5_attributmodifikatorwert) {
        this.shr5_attributmodifikatorwerts.add(shr5_attributmodifikatorwert);
    }

}