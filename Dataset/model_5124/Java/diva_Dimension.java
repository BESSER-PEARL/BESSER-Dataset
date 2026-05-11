





import java.util.List;
import java.util.ArrayList;

public class diva_Dimension extends NamedElement {

    private String upper;
    private String lower;





    private diva_VariabilityModel diva_variabilitymodel;




    private diva_Variant diva_variant;




    private List<diva_Property> diva_propertys;




    private List<diva_Variant> diva_variants;


    public diva_Dimension(
        String upper,        String lower    ) {
        super(
        );
        this.upper = upper;
        this.lower = lower;
        this.diva_propertys = new ArrayList<>();
        this.diva_variants = new ArrayList<>();
    }

    public diva_Dimension(
        String upper,        String lower        ArrayList<diva_Property> diva_propertys,        ArrayList<diva_Variant> diva_variants    ) {
        this.upper = upper;
        this.lower = lower;
        this.diva_propertys = diva_propertys;
        this.diva_variants = diva_variants;
    }

    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }
    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }

    public diva_VariabilityModel getDiva_variabilitymodel() {
        return diva_variabilitymodel;
    }

    public void setDiva_variabilitymodel(diva_VariabilityModel diva_variabilitymodel) {
        this.diva_variabilitymodel = diva_variabilitymodel;
    }
    public diva_Variant getDiva_variant() {
        return diva_variant;
    }

    public void setDiva_variant(diva_Variant diva_variant) {
        this.diva_variant = diva_variant;
    }
    public List<diva_Property> getDiva_propertys() {
        return diva_propertys;
    }

    public void addDiva_property(Diva_property diva_property) {
        this.diva_propertys.add(diva_property);
    }
    public List<diva_Variant> getDiva_variants() {
        return diva_variants;
    }

    public void addDiva_variant(Diva_variant diva_variant) {
        this.diva_variants.add(diva_variant);
    }

}