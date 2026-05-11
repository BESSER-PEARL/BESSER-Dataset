





import java.util.List;
import java.util.ArrayList;

public class aadl2_Property extends AbstractNamedValue, BasicProperty {

    private String inherit;
    private String emptyListDefault;





    private aadl2_PropertyExpression aadl2_propertyexpression;




    private List<aadl2_PropertyOwner> aadl2_propertyowners;




    private aadl2_PropertyAssociation aadl2_propertyassociation;


    public aadl2_Property(
        String inherit,        String emptyListDefault    ) {
        super(
        );
        this.inherit = inherit;
        this.emptyListDefault = emptyListDefault;
        this.aadl2_propertyowners = new ArrayList<>();
    }

    public aadl2_Property(
        String inherit,        String emptyListDefault        ArrayList<aadl2_PropertyOwner> aadl2_propertyowners    ) {
        this.inherit = inherit;
        this.emptyListDefault = emptyListDefault;
        this.aadl2_propertyowners = aadl2_propertyowners;
    }

    public String getInherit() {
        return inherit;
    }

    public void setInherit(String inherit) {
        this.inherit = inherit;
    }
    public String getEmptylistdefault() {
        return emptyListDefault;
    }

    public void setEmptylistdefault(String emptyListDefault) {
        this.emptyListDefault = emptyListDefault;
    }

    public aadl2_PropertyExpression getAadl2_propertyexpression() {
        return aadl2_propertyexpression;
    }

    public void setAadl2_propertyexpression(aadl2_PropertyExpression aadl2_propertyexpression) {
        this.aadl2_propertyexpression = aadl2_propertyexpression;
    }
    public List<aadl2_PropertyOwner> getAadl2_propertyowners() {
        return aadl2_propertyowners;
    }

    public void addAadl2_propertyowner(Aadl2_propertyowner aadl2_propertyowner) {
        this.aadl2_propertyowners.add(aadl2_propertyowner);
    }
    public aadl2_PropertyAssociation getAadl2_propertyassociation() {
        return aadl2_propertyassociation;
    }

    public void setAadl2_propertyassociation(aadl2_PropertyAssociation aadl2_propertyassociation) {
        this.aadl2_propertyassociation = aadl2_propertyassociation;
    }

}