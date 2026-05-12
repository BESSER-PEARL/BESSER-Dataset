





import java.util.List;
import java.util.ArrayList;

public class UML2_Relationship extends Element {






    private List<UML2_Element> uml2_elements;


    public UML2_Relationship(
    ) {
        super(
        );
        this.uml2_elements = new ArrayList<>();
    }

    public UML2_Relationship(
        ArrayList<UML2_Element> uml2_elements    ) {
        this.uml2_elements = uml2_elements;
    }


    public List<UML2_Element> getUml2_elements() {
        return uml2_elements;
    }

    public void addUml2_element(Uml2_element uml2_element) {
        this.uml2_elements.add(uml2_element);
    }

}