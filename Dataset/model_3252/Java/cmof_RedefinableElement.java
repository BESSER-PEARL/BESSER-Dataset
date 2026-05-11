





import java.util.List;
import java.util.ArrayList;

public class cmof_RedefinableElement extends NamedElement {

    private String isLeaf;





    private List<cmof_Classifier> cmof_classifiers;




    private cmof_RedefinableElement cmof_redefinableelement;


    public cmof_RedefinableElement(
        String isLeaf    ) {
        super(
        );
        this.isLeaf = isLeaf;
        this.cmof_classifiers = new ArrayList<>();
    }

    public cmof_RedefinableElement(
        String isLeaf        ArrayList<cmof_Classifier> cmof_classifiers    ) {
        this.isLeaf = isLeaf;
        this.cmof_classifiers = cmof_classifiers;
    }

    public String getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(String isLeaf) {
        this.isLeaf = isLeaf;
    }

    public List<cmof_Classifier> getCmof_classifiers() {
        return cmof_classifiers;
    }

    public void addCmof_classifier(Cmof_classifier cmof_classifier) {
        this.cmof_classifiers.add(cmof_classifier);
    }
    public cmof_RedefinableElement getCmof_redefinableelement() {
        return cmof_redefinableelement;
    }

    public void setCmof_redefinableelement(cmof_RedefinableElement cmof_redefinableelement) {
        this.cmof_redefinableelement = cmof_redefinableelement;
    }

}