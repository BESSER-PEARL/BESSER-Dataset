





import java.util.List;
import java.util.ArrayList;

public class classes_RedefinableElement extends NamedElement {

    private boolean leaf;





    private List<classes_RedefinableElement> classes_redefinableelements;


    public classes_RedefinableElement(
        boolean leaf    ) {
        super(
        );
        this.leaf = leaf;
        this.classes_redefinableelements = new ArrayList<>();
    }

    public classes_RedefinableElement(
        boolean leaf        ArrayList<classes_RedefinableElement> classes_redefinableelements    ) {
        this.leaf = leaf;
        this.classes_redefinableelements = classes_redefinableelements;
    }

    public boolean getLeaf() {
        return leaf;
    }

    public void setLeaf(boolean leaf) {
        this.leaf = leaf;
    }

    public List<classes_RedefinableElement> getClasses_redefinableelements() {
        return classes_redefinableelements;
    }

    public void addClasses_redefinableelement(Classes_redefinableelement classes_redefinableelement) {
        this.classes_redefinableelements.add(classes_redefinableelement);
    }

}