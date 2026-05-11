





import java.util.List;
import java.util.ArrayList;

public class umlClass_Element  {






    private umlClass_Element umlclass_element;




    private List<umlClass_Element> umlclass_elements;


    public umlClass_Element(
    ) {
        this.umlclass_elements = new ArrayList<>();
    }

    public umlClass_Element(
        ArrayList<umlClass_Element> umlclass_elements    ) {
        this.umlclass_elements = umlclass_elements;
    }


    public umlClass_Element getUmlclass_element() {
        return umlclass_element;
    }

    public void setUmlclass_element(umlClass_Element umlclass_element) {
        this.umlclass_element = umlclass_element;
    }
    public List<umlClass_Element> getUmlclass_elements() {
        return umlclass_elements;
    }

    public void addUmlclass_element(Umlclass_element umlclass_element) {
        this.umlclass_elements.add(umlclass_element);
    }

}