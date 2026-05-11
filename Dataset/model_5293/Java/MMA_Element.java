





import java.util.List;
import java.util.ArrayList;

public class MMA_Element  {

    private String name;





    private List<Element> elements;




    private List<Element> elements;




    private Root root;


    public MMA_Element(
        String name    ) {
        this.name = name;
        this.elements = new ArrayList<>();
        this.elements = new ArrayList<>();
    }

    public MMA_Element(
        String name        ArrayList<Element> elements,        ArrayList<Element> elements    ) {
        this.name = name;
        this.elements = elements;
        this.elements = elements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Element> getElements() {
        return elements;
    }

    public void addElement(Element element) {
        this.elements.add(element);
    }
    public List<Element> getElements() {
        return elements;
    }

    public void addElement(Element element) {
        this.elements.add(element);
    }
    public Root getRoot() {
        return root;
    }

    public void setRoot(Root root) {
        this.root = root;
    }

}