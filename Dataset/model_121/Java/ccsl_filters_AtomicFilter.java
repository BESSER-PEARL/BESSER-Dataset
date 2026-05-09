





import java.util.List;
import java.util.ArrayList;

public class ccsl_filters_AtomicFilter extends Filter {






    private List<Element> elements;


    public ccsl_filters_AtomicFilter(
    ) {
        super(
        );
        this.elements = new ArrayList<>();
    }

    public ccsl_filters_AtomicFilter(
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