





import java.util.List;
import java.util.ArrayList;

public class RefUML_DirectedRelationship extends Relationship {






    private List<RefUML_Element> refuml_elements;




    private List<RefUML_Element> refuml_elements;


    public RefUML_DirectedRelationship(
    ) {
        super(
        );
        this.refuml_elements = new ArrayList<>();
        this.refuml_elements = new ArrayList<>();
    }

    public RefUML_DirectedRelationship(
        ArrayList<RefUML_Element> refuml_elements,        ArrayList<RefUML_Element> refuml_elements    ) {
        this.refuml_elements = refuml_elements;
        this.refuml_elements = refuml_elements;
    }


    public List<RefUML_Element> getRefuml_elements() {
        return refuml_elements;
    }

    public void addRefuml_element(Refuml_element refuml_element) {
        this.refuml_elements.add(refuml_element);
    }
    public List<RefUML_Element> getRefuml_elements() {
        return refuml_elements;
    }

    public void addRefuml_element(Refuml_element refuml_element) {
        this.refuml_elements.add(refuml_element);
    }

}