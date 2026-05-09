





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_RedefinableElement extends NamedElement {

    private String isLeaf;





    private List<uml3_0_0_Classifier> uml3_0_0_classifiers;




    private List<uml3_0_0_RedefinableElement> uml3_0_0_redefinableelements;


    public uml3_0_0_RedefinableElement(
        String isLeaf    ) {
        super(
        );
        this.isLeaf = isLeaf;
        this.uml3_0_0_classifiers = new ArrayList<>();
        this.uml3_0_0_redefinableelements = new ArrayList<>();
    }

    public uml3_0_0_RedefinableElement(
        String isLeaf        ArrayList<uml3_0_0_Classifier> uml3_0_0_classifiers,        ArrayList<uml3_0_0_RedefinableElement> uml3_0_0_redefinableelements    ) {
        this.isLeaf = isLeaf;
        this.uml3_0_0_classifiers = uml3_0_0_classifiers;
        this.uml3_0_0_redefinableelements = uml3_0_0_redefinableelements;
    }

    public String getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(String isLeaf) {
        this.isLeaf = isLeaf;
    }

    public List<uml3_0_0_Classifier> getUml3_0_0_classifiers() {
        return uml3_0_0_classifiers;
    }

    public void addUml3_0_0_classifier(Uml3_0_0_classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifiers.add(uml3_0_0_classifier);
    }
    public List<uml3_0_0_RedefinableElement> getUml3_0_0_redefinableelements() {
        return uml3_0_0_redefinableelements;
    }

    public void addUml3_0_0_redefinableelement(Uml3_0_0_redefinableelement uml3_0_0_redefinableelement) {
        this.uml3_0_0_redefinableelements.add(uml3_0_0_redefinableelement);
    }

}