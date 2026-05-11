





import java.util.List;
import java.util.ArrayList;

public class aadl2_ContainmentPathElement extends Element {

    private String annexName;





    private aadl2_ContainmentPathElement aadl2_containmentpathelement;




    private aadl2_ContainedNamedElement aadl2_containednamedelement;




    private aadl2_ContainedNamedElement aadl2_containednamedelement;


    public aadl2_ContainmentPathElement(
        String annexName    ) {
        super(
        );
        this.annexName = annexName;
    }


    public String getAnnexname() {
        return annexName;
    }

    public void setAnnexname(String annexName) {
        this.annexName = annexName;
    }

    public aadl2_ContainmentPathElement getAadl2_containmentpathelement() {
        return aadl2_containmentpathelement;
    }

    public void setAadl2_containmentpathelement(aadl2_ContainmentPathElement aadl2_containmentpathelement) {
        this.aadl2_containmentpathelement = aadl2_containmentpathelement;
    }
    public aadl2_ContainedNamedElement getAadl2_containednamedelement() {
        return aadl2_containednamedelement;
    }

    public void setAadl2_containednamedelement(aadl2_ContainedNamedElement aadl2_containednamedelement) {
        this.aadl2_containednamedelement = aadl2_containednamedelement;
    }
    public aadl2_ContainedNamedElement getAadl2_containednamedelement() {
        return aadl2_containednamedelement;
    }

    public void setAadl2_containednamedelement(aadl2_ContainedNamedElement aadl2_containednamedelement) {
        this.aadl2_containednamedelement = aadl2_containednamedelement;
    }

}