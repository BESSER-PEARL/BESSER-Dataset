





import java.util.List;
import java.util.ArrayList;

public class aadl2_ContainedNamedElement extends Element {






    private List<aadl2_ContainmentPathElement> aadl2_containmentpathelements;


    public aadl2_ContainedNamedElement(
    ) {
        super(
        );
        this.aadl2_containmentpathelements = new ArrayList<>();
    }

    public aadl2_ContainedNamedElement(
        ArrayList<aadl2_ContainmentPathElement> aadl2_containmentpathelements    ) {
        this.aadl2_containmentpathelements = aadl2_containmentpathelements;
    }


    public List<aadl2_ContainmentPathElement> getAadl2_containmentpathelements() {
        return aadl2_containmentpathelements;
    }

    public void addAadl2_containmentpathelement(Aadl2_containmentpathelement aadl2_containmentpathelement) {
        this.aadl2_containmentpathelements.add(aadl2_containmentpathelement);
    }

}