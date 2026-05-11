





import java.util.List;
import java.util.ArrayList;

public class diva_Variant extends NamedElement {






    private List<diva_PropertyValue> diva_propertyvalues;




    private diva_VariantTerm diva_variantterm;




    private diva_Dimension diva_dimension;




    private diva_Dimension diva_dimension;


    public diva_Variant(
    ) {
        super(
        );
        this.diva_propertyvalues = new ArrayList<>();
    }

    public diva_Variant(
        ArrayList<diva_PropertyValue> diva_propertyvalues    ) {
        this.diva_propertyvalues = diva_propertyvalues;
    }


    public List<diva_PropertyValue> getDiva_propertyvalues() {
        return diva_propertyvalues;
    }

    public void addDiva_propertyvalue(Diva_propertyvalue diva_propertyvalue) {
        this.diva_propertyvalues.add(diva_propertyvalue);
    }
    public diva_VariantTerm getDiva_variantterm() {
        return diva_variantterm;
    }

    public void setDiva_variantterm(diva_VariantTerm diva_variantterm) {
        this.diva_variantterm = diva_variantterm;
    }
    public diva_Dimension getDiva_dimension() {
        return diva_dimension;
    }

    public void setDiva_dimension(diva_Dimension diva_dimension) {
        this.diva_dimension = diva_dimension;
    }
    public diva_Dimension getDiva_dimension() {
        return diva_dimension;
    }

    public void setDiva_dimension(diva_Dimension diva_dimension) {
        this.diva_dimension = diva_dimension;
    }

}