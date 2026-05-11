





import java.util.List;
import java.util.ArrayList;

public class diva_Dimension extends NamedElement {

    private String upper;
    private String lower;





    private List<diva_Variant> diva_variants;




    private diva_Variant diva_variant;




    private List<diva_MultiplicityConstraint> diva_multiplicityconstraints;


    public diva_Dimension(
        String upper,        String lower    ) {
        super(
        );
        this.upper = upper;
        this.lower = lower;
        this.diva_variants = new ArrayList<>();
        this.diva_multiplicityconstraints = new ArrayList<>();
    }

    public diva_Dimension(
        String upper,        String lower        ArrayList<diva_Variant> diva_variants,        ArrayList<diva_MultiplicityConstraint> diva_multiplicityconstraints    ) {
        this.upper = upper;
        this.lower = lower;
        this.diva_variants = diva_variants;
        this.diva_multiplicityconstraints = diva_multiplicityconstraints;
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

    public List<diva_Variant> getDiva_variants() {
        return diva_variants;
    }

    public void addDiva_variant(Diva_variant diva_variant) {
        this.diva_variants.add(diva_variant);
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

}