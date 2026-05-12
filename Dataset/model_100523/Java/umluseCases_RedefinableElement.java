





import java.util.List;
import java.util.ArrayList;

public class umluseCases_RedefinableElement extends NamedElement {

    private String isLeaf;





    private List<umluseCases_RedefinableElement> umlusecases_redefinableelements;


    public umluseCases_RedefinableElement(
        String isLeaf    ) {
        super(
        );
        this.isLeaf = isLeaf;
        this.umlusecases_redefinableelements = new ArrayList<>();
    }

    public umluseCases_RedefinableElement(
        String isLeaf        ArrayList<umluseCases_RedefinableElement> umlusecases_redefinableelements    ) {
        this.isLeaf = isLeaf;
        this.umlusecases_redefinableelements = umlusecases_redefinableelements;
    }

    public String getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(String isLeaf) {
        this.isLeaf = isLeaf;
    }

    public List<umluseCases_RedefinableElement> getUmlusecases_redefinableelements() {
        return umlusecases_redefinableelements;
    }

    public void addUmlusecases_redefinableelement(Umlusecases_redefinableelement umlusecases_redefinableelement) {
        this.umlusecases_redefinableelements.add(umlusecases_redefinableelement);
    }

}