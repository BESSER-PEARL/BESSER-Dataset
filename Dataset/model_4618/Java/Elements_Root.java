





import java.util.List;
import java.util.ArrayList;

public class Elements_Root extends IdentifiedElement {

    private String name;





    private List<Elements_NamedElement> elements_namedelements;


    public Elements_Root(
        String name    ) {
        super(
        );
        this.name = name;
        this.elements_namedelements = new ArrayList<>();
    }

    public Elements_Root(
        String name        ArrayList<Elements_NamedElement> elements_namedelements    ) {
        this.name = name;
        this.elements_namedelements = elements_namedelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Elements_NamedElement> getElements_namedelements() {
        return elements_namedelements;
    }

    public void addElements_namedelement(Elements_namedelement elements_namedelement) {
        this.elements_namedelements.add(elements_namedelement);
    }

}