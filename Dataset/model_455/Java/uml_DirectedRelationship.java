





import java.util.List;
import java.util.ArrayList;

public class uml_DirectedRelationship extends Relationship {






    private List<uml_Element> uml_elements;




    private List<uml_Element> uml_elements;


    public uml_DirectedRelationship(
    ) {
        super(
        );
        this.uml_elements = new ArrayList<>();
        this.uml_elements = new ArrayList<>();
    }

    public uml_DirectedRelationship(
        ArrayList<uml_Element> uml_elements,        ArrayList<uml_Element> uml_elements    ) {
        this.uml_elements = uml_elements;
        this.uml_elements = uml_elements;
    }


    public List<uml_Element> getUml_elements() {
        return uml_elements;
    }

    public void addUml_element(Uml_element uml_element) {
        this.uml_elements.add(uml_element);
    }
    public List<uml_Element> getUml_elements() {
        return uml_elements;
    }

    public void addUml_element(Uml_element uml_element) {
        this.uml_elements.add(uml_element);
    }

}