





import java.util.List;
import java.util.ArrayList;

public class aadl2_PropertyAssociation extends Element {

    private String append;
    private String constant;





    private List<aadl2_ModalPropertyValue> aadl2_modalpropertyvalues;




    private List<aadl2_ContainedNamedElement> aadl2_containednamedelements;


    public aadl2_PropertyAssociation(
        String append,        String constant    ) {
        super(
        );
        this.append = append;
        this.constant = constant;
        this.aadl2_modalpropertyvalues = new ArrayList<>();
        this.aadl2_containednamedelements = new ArrayList<>();
    }

    public aadl2_PropertyAssociation(
        String append,        String constant        ArrayList<aadl2_ModalPropertyValue> aadl2_modalpropertyvalues,        ArrayList<aadl2_ContainedNamedElement> aadl2_containednamedelements    ) {
        this.append = append;
        this.constant = constant;
        this.aadl2_modalpropertyvalues = aadl2_modalpropertyvalues;
        this.aadl2_containednamedelements = aadl2_containednamedelements;
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

    public List<aadl2_ModalPropertyValue> getAadl2_modalpropertyvalues() {
        return aadl2_modalpropertyvalues;
    }

    public void addAadl2_modalpropertyvalue(Aadl2_modalpropertyvalue aadl2_modalpropertyvalue) {
        this.aadl2_modalpropertyvalues.add(aadl2_modalpropertyvalue);
    }
    public List<aadl2_ContainedNamedElement> getAadl2_containednamedelements() {
        return aadl2_containednamedelements;
    }

    public void addAadl2_containednamedelement(Aadl2_containednamedelement aadl2_containednamedelement) {
        this.aadl2_containednamedelements.add(aadl2_containednamedelement);
    }

}