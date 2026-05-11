





import java.util.List;
import java.util.ArrayList;

public class Elements_Node extends NamedElement {






    private List<Elements_NamedElement> elements_namedelements;


    public Elements_Node(
    ) {
        super(
        );
        this.elements_namedelements = new ArrayList<>();
    }

    public Elements_Node(
        ArrayList<Elements_NamedElement> elements_namedelements    ) {
        this.elements_namedelements = elements_namedelements;
    }


    public List<Elements_NamedElement> getElements_namedelements() {
        return elements_namedelements;
    }

    public void addElements_namedelement(Elements_namedelement elements_namedelement) {
        this.elements_namedelements.add(elements_namedelement);
    }

}