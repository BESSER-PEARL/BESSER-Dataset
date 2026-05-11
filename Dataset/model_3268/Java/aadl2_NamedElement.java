





import java.util.List;
import java.util.ArrayList;

public class aadl2_NamedElement extends Element {

    private String name;
    private String qualifiedName;





    private aadl2_Classifier aadl2_classifier;




    private aadl2_ContainmentPathElement aadl2_containmentpathelement;




    private List<aadl2_PropertyAssociation> aadl2_propertyassociations;


    public aadl2_NamedElement(
        String name,        String qualifiedName    ) {
        super(
        );
        this.name = name;
        this.qualifiedName = qualifiedName;
        this.aadl2_propertyassociations = new ArrayList<>();
    }

    public aadl2_NamedElement(
        String name,        String qualifiedName        ArrayList<aadl2_PropertyAssociation> aadl2_propertyassociations    ) {
        this.name = name;
        this.qualifiedName = qualifiedName;
        this.aadl2_propertyassociations = aadl2_propertyassociations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }

    public aadl2_Classifier getAadl2_classifier() {
        return aadl2_classifier;
    }

    public void setAadl2_classifier(aadl2_Classifier aadl2_classifier) {
        this.aadl2_classifier = aadl2_classifier;
    }
    public aadl2_ContainmentPathElement getAadl2_containmentpathelement() {
        return aadl2_containmentpathelement;
    }

    public void setAadl2_containmentpathelement(aadl2_ContainmentPathElement aadl2_containmentpathelement) {
        this.aadl2_containmentpathelement = aadl2_containmentpathelement;
    }
    public List<aadl2_PropertyAssociation> getAadl2_propertyassociations() {
        return aadl2_propertyassociations;
    }

    public void addAadl2_propertyassociation(Aadl2_propertyassociation aadl2_propertyassociation) {
        this.aadl2_propertyassociations.add(aadl2_propertyassociation);
    }

}