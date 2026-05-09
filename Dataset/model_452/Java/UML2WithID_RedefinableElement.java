





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_RedefinableElement extends NamedElement {

    private boolean isLeaf;





    private List<UML2WithID_Classifier> uml2withid_classifiers;


    public UML2WithID_RedefinableElement(
        boolean isLeaf    ) {
        super(
        );
        this.isLeaf = isLeaf;
        this.uml2withid_classifiers = new ArrayList<>();
    }

    public UML2WithID_RedefinableElement(
        boolean isLeaf        ArrayList<UML2WithID_Classifier> uml2withid_classifiers    ) {
        this.isLeaf = isLeaf;
        this.uml2withid_classifiers = uml2withid_classifiers;
    }

    public boolean getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(boolean isLeaf) {
        this.isLeaf = isLeaf;
    }

    public List<UML2WithID_Classifier> getUml2withid_classifiers() {
        return uml2withid_classifiers;
    }

    public void addUml2withid_classifier(Uml2withid_classifier uml2withid_classifier) {
        this.uml2withid_classifiers.add(uml2withid_classifier);
    }

}