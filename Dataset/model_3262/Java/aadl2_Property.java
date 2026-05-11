





import java.util.List;
import java.util.ArrayList;

public class aadl2_Property extends BasicProperty, AbstractNamedValue, ArraySizeProperty {

    private String emptyListDefault;
    private String inherit;





    private List<aadl2_Classifier> aadl2_classifiers;




    private aadl2_PropertyAssociation aadl2_propertyassociation;




    private aadl2_PropertyExpression aadl2_propertyexpression;




    private List<aadl2_PropertyOwner> aadl2_propertyowners;




    private aadl2_PropertySet aadl2_propertyset;


    public aadl2_Property(
        String emptyListDefault,        String inherit    ) {
        super(
        );
        this.emptyListDefault = emptyListDefault;
        this.inherit = inherit;
        this.aadl2_classifiers = new ArrayList<>();
        this.aadl2_propertyowners = new ArrayList<>();
    }

    public aadl2_Property(
        String emptyListDefault,        String inherit        ArrayList<aadl2_Classifier> aadl2_classifiers,        ArrayList<aadl2_PropertyOwner> aadl2_propertyowners    ) {
        this.emptyListDefault = emptyListDefault;
        this.inherit = inherit;
        this.aadl2_classifiers = aadl2_classifiers;
        this.aadl2_propertyowners = aadl2_propertyowners;
    }

    public String getEmptylistdefault() {
        return emptyListDefault;
    }

    public void setEmptylistdefault(String emptyListDefault) {
        this.emptyListDefault = emptyListDefault;
    }
    public String getInherit() {
        return inherit;
    }

    public void setInherit(String inherit) {
        this.inherit = inherit;
    }

    public List<aadl2_Classifier> getAadl2_classifiers() {
        return aadl2_classifiers;
    }

    public void addAadl2_classifier(Aadl2_classifier aadl2_classifier) {
        this.aadl2_classifiers.add(aadl2_classifier);
    }
    public aadl2_PropertyAssociation getAadl2_propertyassociation() {
        return aadl2_propertyassociation;
    }

    public void setAadl2_propertyassociation(aadl2_PropertyAssociation aadl2_propertyassociation) {
        this.aadl2_propertyassociation = aadl2_propertyassociation;
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
    public aadl2_PropertySet getAadl2_propertyset() {
        return aadl2_propertyset;
    }

    public void setAadl2_propertyset(aadl2_PropertySet aadl2_propertyset) {
        this.aadl2_propertyset = aadl2_propertyset;
    }

}