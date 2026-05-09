





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_RedefinableElement extends NamedElement {

    private boolean isLeaf;





    private List<CompleteDSLPckg_RedefinableElement> completedslpckg_redefinableelements;


    public CompleteDSLPckg_RedefinableElement(
        boolean isLeaf    ) {
        super(
        );
        this.isLeaf = isLeaf;
        this.completedslpckg_redefinableelements = new ArrayList<>();
    }

    public CompleteDSLPckg_RedefinableElement(
        boolean isLeaf        ArrayList<CompleteDSLPckg_RedefinableElement> completedslpckg_redefinableelements    ) {
        this.isLeaf = isLeaf;
        this.completedslpckg_redefinableelements = completedslpckg_redefinableelements;
    }

    public boolean getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(boolean isLeaf) {
        this.isLeaf = isLeaf;
    }

    public List<CompleteDSLPckg_RedefinableElement> getCompletedslpckg_redefinableelements() {
        return completedslpckg_redefinableelements;
    }

    public void addCompletedslpckg_redefinableelement(Completedslpckg_redefinableelement completedslpckg_redefinableelement) {
        this.completedslpckg_redefinableelements.add(completedslpckg_redefinableelement);
    }

}