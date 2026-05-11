





import java.util.List;
import java.util.ArrayList;

public class aadl2_NamedElement extends Element {

    private String qualifiedName;
    private String name;





    private aadl2_ContainmentPathElement aadl2_containmentpathelement;




    private List<aadl2_PropertyAssociation> aadl2_propertyassociations;


    public aadl2_NamedElement(
        String qualifiedName,        String name    ) {
        super(
        );
        this.qualifiedName = qualifiedName;
        this.name = name;
        this.aadl2_propertyassociations = new ArrayList<>();
    }

    public aadl2_NamedElement(
        String qualifiedName,        String name        ArrayList<aadl2_PropertyAssociation> aadl2_propertyassociations    ) {
        this.qualifiedName = qualifiedName;
        this.name = name;
        this.aadl2_propertyassociations = aadl2_propertyassociations;
    }

    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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