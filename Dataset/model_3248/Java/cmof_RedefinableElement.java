





import java.util.List;
import java.util.ArrayList;

public class cmof_RedefinableElement extends NamedElement {

    private String isLeaf;





    private List<cmof_RedefinableElement> cmof_redefinableelements;




    private List<cmof_Classifier> cmof_classifiers;


    public cmof_RedefinableElement(
        String isLeaf    ) {
        super(
        );
        this.isLeaf = isLeaf;
        this.cmof_redefinableelements = new ArrayList<>();
        this.cmof_classifiers = new ArrayList<>();
    }

    public cmof_RedefinableElement(
        String isLeaf        ArrayList<cmof_RedefinableElement> cmof_redefinableelements,        ArrayList<cmof_Classifier> cmof_classifiers    ) {
        this.isLeaf = isLeaf;
        this.cmof_redefinableelements = cmof_redefinableelements;
        this.cmof_classifiers = cmof_classifiers;
    }

    public String getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(String isLeaf) {
        this.isLeaf = isLeaf;
    }

    public List<cmof_RedefinableElement> getCmof_redefinableelements() {
        return cmof_redefinableelements;
    }

    public void addCmof_redefinableelement(Cmof_redefinableelement cmof_redefinableelement) {
        this.cmof_redefinableelements.add(cmof_redefinableelement);
    }
    public List<cmof_Classifier> getCmof_classifiers() {
        return cmof_classifiers;
    }

    public void addCmof_classifier(Cmof_classifier cmof_classifier) {
        this.cmof_classifiers.add(cmof_classifier);
    }

}