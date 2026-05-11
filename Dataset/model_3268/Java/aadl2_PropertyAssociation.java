





import java.util.List;
import java.util.ArrayList;

public class aadl2_PropertyAssociation extends Element {

    private String append;
    private String constant;





    private List<aadl2_ContainedNamedElement> aadl2_containednamedelements;




    private List<aadl2_ModalPropertyValue> aadl2_modalpropertyvalues;




    private List<aadl2_Classifier> aadl2_classifiers;




    private aadl2_Property aadl2_property;


    public aadl2_PropertyAssociation(
        String append,        String constant    ) {
        super(
        );
        this.append = append;
        this.constant = constant;
        this.aadl2_containednamedelements = new ArrayList<>();
        this.aadl2_modalpropertyvalues = new ArrayList<>();
        this.aadl2_classifiers = new ArrayList<>();
    }

    public aadl2_PropertyAssociation(
        String append,        String constant        ArrayList<aadl2_ContainedNamedElement> aadl2_containednamedelements,        ArrayList<aadl2_ModalPropertyValue> aadl2_modalpropertyvalues,        ArrayList<aadl2_Classifier> aadl2_classifiers    ) {
        this.append = append;
        this.constant = constant;
        this.aadl2_containednamedelements = aadl2_containednamedelements;
        this.aadl2_modalpropertyvalues = aadl2_modalpropertyvalues;
        this.aadl2_classifiers = aadl2_classifiers;
    }

    public String getAppend() {
        return append;
    }

    public void setAppend(String append) {
        this.append = append;
    }
    public String getConstant() {
        return constant;
    }

    public void setConstant(String constant) {
        this.constant = constant;
    }

    public List<aadl2_ContainedNamedElement> getAadl2_containednamedelements() {
        return aadl2_containednamedelements;
    }

    public void addAadl2_containednamedelement(Aadl2_containednamedelement aadl2_containednamedelement) {
        this.aadl2_containednamedelements.add(aadl2_containednamedelement);
    }
    public List<aadl2_ModalPropertyValue> getAadl2_modalpropertyvalues() {
        return aadl2_modalpropertyvalues;
    }

    public void addAadl2_modalpropertyvalue(Aadl2_modalpropertyvalue aadl2_modalpropertyvalue) {
        this.aadl2_modalpropertyvalues.add(aadl2_modalpropertyvalue);
    }
    public List<aadl2_Classifier> getAadl2_classifiers() {
        return aadl2_classifiers;
    }

    public void addAadl2_classifier(Aadl2_classifier aadl2_classifier) {
        this.aadl2_classifiers.add(aadl2_classifier);
    }
    public aadl2_Property getAadl2_property() {
        return aadl2_property;
    }

    public void setAadl2_property(aadl2_Property aadl2_property) {
        this.aadl2_property = aadl2_property;
    }

}