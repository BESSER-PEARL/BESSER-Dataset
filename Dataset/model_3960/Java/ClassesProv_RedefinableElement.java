





import java.util.List;
import java.util.ArrayList;

public class ClassesProv_RedefinableElement extends NamedElement {

    private boolean isLeaf;





    private List<ClassesProv_RedefinableElement> classesprov_redefinableelements;


    public ClassesProv_RedefinableElement(
        boolean isLeaf    ) {
        super(
        );
        this.isLeaf = isLeaf;
        this.classesprov_redefinableelements = new ArrayList<>();
    }

    public ClassesProv_RedefinableElement(
        boolean isLeaf        ArrayList<ClassesProv_RedefinableElement> classesprov_redefinableelements    ) {
        this.isLeaf = isLeaf;
        this.classesprov_redefinableelements = classesprov_redefinableelements;
    }

    public boolean getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(boolean isLeaf) {
        this.isLeaf = isLeaf;
    }

    public List<ClassesProv_RedefinableElement> getClassesprov_redefinableelements() {
        return classesprov_redefinableelements;
    }

    public void addClassesprov_redefinableelement(Classesprov_redefinableelement classesprov_redefinableelement) {
        this.classesprov_redefinableelements.add(classesprov_redefinableelement);
    }

}