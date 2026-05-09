





import java.util.List;
import java.util.ArrayList;

public class uml_Relationship extends Element {






    private List<uml_Element> uml_elements;


    public uml_Relationship(
    ) {
        super(
        );
        this.uml_elements = new ArrayList<>();
    }

    public uml_Relationship(
        ArrayList<uml_Element> uml_elements    ) {
        this.uml_elements = uml_elements;
    }


    public List<uml_Element> getUml_elements() {
        return uml_elements;
    }

    public void addUml_element(Uml_element uml_element) {
        this.uml_elements.add(uml_element);
    }

}