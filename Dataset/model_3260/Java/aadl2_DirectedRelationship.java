





import java.util.List;
import java.util.ArrayList;

public class aadl2_DirectedRelationship extends Relationship {






    private List<aadl2_Element> aadl2_elements;




    private List<aadl2_Element> aadl2_elements;


    public aadl2_DirectedRelationship(
    ) {
        super(
        );
        this.aadl2_elements = new ArrayList<>();
        this.aadl2_elements = new ArrayList<>();
    }

    public aadl2_DirectedRelationship(
        ArrayList<aadl2_Element> aadl2_elements,        ArrayList<aadl2_Element> aadl2_elements    ) {
        this.aadl2_elements = aadl2_elements;
        this.aadl2_elements = aadl2_elements;
    }


    public List<aadl2_Element> getAadl2_elements() {
        return aadl2_elements;
    }

    public void addAadl2_element(Aadl2_element aadl2_element) {
        this.aadl2_elements.add(aadl2_element);
    }
    public List<aadl2_Element> getAadl2_elements() {
        return aadl2_elements;
    }

    public void addAadl2_element(Aadl2_element aadl2_element) {
        this.aadl2_elements.add(aadl2_element);
    }

}