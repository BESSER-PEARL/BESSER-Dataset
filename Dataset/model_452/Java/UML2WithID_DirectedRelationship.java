





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_DirectedRelationship extends Relationship {






    private List<UML2WithID_Element> uml2withid_elements;




    private List<UML2WithID_Element> uml2withid_elements;


    public UML2WithID_DirectedRelationship(
    ) {
        super(
        );
        this.uml2withid_elements = new ArrayList<>();
        this.uml2withid_elements = new ArrayList<>();
    }

    public UML2WithID_DirectedRelationship(
        ArrayList<UML2WithID_Element> uml2withid_elements,        ArrayList<UML2WithID_Element> uml2withid_elements    ) {
        this.uml2withid_elements = uml2withid_elements;
        this.uml2withid_elements = uml2withid_elements;
    }


    public List<UML2WithID_Element> getUml2withid_elements() {
        return uml2withid_elements;
    }

    public void addUml2withid_element(Uml2withid_element uml2withid_element) {
        this.uml2withid_elements.add(uml2withid_element);
    }
    public List<UML2WithID_Element> getUml2withid_elements() {
        return uml2withid_elements;
    }

    public void addUml2withid_element(Uml2withid_element uml2withid_element) {
        this.uml2withid_elements.add(uml2withid_element);
    }

}