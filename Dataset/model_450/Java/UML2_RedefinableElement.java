





import java.util.List;
import java.util.ArrayList;

public class UML2_RedefinableElement extends NamedElement {

    private boolean isLeaf;





    private List<UML2_Classifier> uml2_classifiers;


    public UML2_RedefinableElement(
        boolean isLeaf    ) {
        super(
        );
        this.isLeaf = isLeaf;
        this.uml2_classifiers = new ArrayList<>();
    }

    public UML2_RedefinableElement(
        boolean isLeaf        ArrayList<UML2_Classifier> uml2_classifiers    ) {
        this.isLeaf = isLeaf;
        this.uml2_classifiers = uml2_classifiers;
    }

    public boolean getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(boolean isLeaf) {
        this.isLeaf = isLeaf;
    }

    public List<UML2_Classifier> getUml2_classifiers() {
        return uml2_classifiers;
    }

    public void addUml2_classifier(Uml2_classifier uml2_classifier) {
        this.uml2_classifiers.add(uml2_classifier);
    }

}