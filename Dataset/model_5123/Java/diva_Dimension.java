





import java.util.List;
import java.util.ArrayList;

public class diva_Dimension extends NamedElement {

    private String lower;
    private String upper;





    private diva_Variant diva_variant;




    private List<diva_MultiplicityConstraint> diva_multiplicityconstraints;




    private List<diva_Variant> diva_variants;




    private List<diva_Property> diva_propertys;




    private diva_VariabilityModel diva_variabilitymodel;


    public diva_Dimension(
        String lower,        String upper    ) {
        super(
        );
        this.lower = lower;
        this.upper = upper;
        this.diva_multiplicityconstraints = new ArrayList<>();
        this.diva_variants = new ArrayList<>();
        this.diva_propertys = new ArrayList<>();
    }

    public diva_Dimension(
        String lower,        String upper        ArrayList<diva_MultiplicityConstraint> diva_multiplicityconstraints,        ArrayList<diva_Variant> diva_variants,        ArrayList<diva_Property> diva_propertys    ) {
        this.lower = lower;
        this.upper = upper;
        this.diva_multiplicityconstraints = diva_multiplicityconstraints;
        this.diva_variants = diva_variants;
        this.diva_propertys = diva_propertys;
    }

    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }

    public diva_Variant getDiva_variant() {
        return diva_variant;
    }

    public void setDiva_variant(diva_Variant diva_variant) {
        this.diva_variant = diva_variant;
    }
    public List<diva_MultiplicityConstraint> getDiva_multiplicityconstraints() {
        return diva_multiplicityconstraints;
    }

    public void addDiva_multiplicityconstraint(Diva_multiplicityconstraint diva_multiplicityconstraint) {
        this.diva_multiplicityconstraints.add(diva_multiplicityconstraint);
    }
    public List<diva_Variant> getDiva_variants() {
        return diva_variants;
    }

    public void addDiva_variant(Diva_variant diva_variant) {
        this.diva_variants.add(diva_variant);
    }
    public List<diva_Property> getDiva_propertys() {
        return diva_propertys;
    }

    public void addDiva_property(Diva_property diva_property) {
        this.diva_propertys.add(diva_property);
    }
    public diva_VariabilityModel getDiva_variabilitymodel() {
        return diva_variabilitymodel;
    }

    public void setDiva_variabilitymodel(diva_VariabilityModel diva_variabilitymodel) {
        this.diva_variabilitymodel = diva_variabilitymodel;
    }

}