





import java.util.List;
import java.util.ArrayList;

public class Classes_Kernel_Constraint extends PackageableElement {






    private Namespace namespace;




    private List<Element> elements;


    public Classes_Kernel_Constraint(
    ) {
        super(
        );
        this.elements = new ArrayList<>();
    }

    public Classes_Kernel_Constraint(
        ArrayList<Element> elements    ) {
        this.elements = elements;
    }


    public Namespace getNamespace() {
        return namespace;
    }

    public void setNamespace(Namespace namespace) {
        this.namespace = namespace;
    }
    public List<Element> getElements() {
        return elements;
    }

    public void addElement(Element element) {
        this.elements.add(element);
    }

}