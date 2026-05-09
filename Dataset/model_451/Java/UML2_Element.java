





import java.util.List;
import java.util.ArrayList;

public class UML2_Element  {






    private UML2_Element uml2_element;




    private List<UML2_Element> uml2_elements;


    public UML2_Element(
    ) {
        this.uml2_elements = new ArrayList<>();
    }

    public UML2_Element(
        ArrayList<UML2_Element> uml2_elements    ) {
        this.uml2_elements = uml2_elements;
    }


    public UML2_Element getUml2_element() {
        return uml2_element;
    }

    public void setUml2_element(UML2_Element uml2_element) {
        this.uml2_element = uml2_element;
    }
    public List<UML2_Element> getUml2_elements() {
        return uml2_elements;
    }

    public void addUml2_element(Uml2_element uml2_element) {
        this.uml2_elements.add(uml2_element);
    }

}