





import java.util.List;
import java.util.ArrayList;

public class aadl2_ContainmentPathElement extends Element {






    private aadl2_ContainedNamedElement aadl2_containednamedelement;




    private aadl2_NamedElement aadl2_namedelement;


    public aadl2_ContainmentPathElement(
    ) {
        super(
        );
    }



    public aadl2_ContainedNamedElement getAadl2_containednamedelement() {
        return aadl2_containednamedelement;
    }

    public void setAadl2_containednamedelement(aadl2_ContainedNamedElement aadl2_containednamedelement) {
        this.aadl2_containednamedelement = aadl2_containednamedelement;
    }
    public aadl2_NamedElement getAadl2_namedelement() {
        return aadl2_namedelement;
    }

    public void setAadl2_namedelement(aadl2_NamedElement aadl2_namedelement) {
        this.aadl2_namedelement = aadl2_namedelement;
    }

}