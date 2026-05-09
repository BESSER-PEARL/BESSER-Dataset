





import java.util.List;
import java.util.ArrayList;

public class ccsl_context_Context  {






    private List<Element> elements;


    public ccsl_context_Context(
    ) {
        this.elements = new ArrayList<>();
    }

    public ccsl_context_Context(
        ArrayList<Element> elements    ) {
        this.elements = elements;
    }


    public List<Element> getElements() {
        return elements;
    }

    public void addElement(Element element) {
        this.elements.add(element);
    }

}