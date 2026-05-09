





import java.util.List;
import java.util.ArrayList;

public class smalluml_Package  {






    private List<smalluml_Element> smalluml_elements;


    public smalluml_Package(
    ) {
        this.smalluml_elements = new ArrayList<>();
    }

    public smalluml_Package(
        ArrayList<smalluml_Element> smalluml_elements    ) {
        this.smalluml_elements = smalluml_elements;
    }


    public List<smalluml_Element> getSmalluml_elements() {
        return smalluml_elements;
    }

    public void addSmalluml_element(Smalluml_element smalluml_element) {
        this.smalluml_elements.add(smalluml_element);
    }

}