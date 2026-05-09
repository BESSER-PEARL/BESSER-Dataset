





import java.util.List;
import java.util.ArrayList;

public class RefUML_RedefinableElement extends NamedElement {

    private String isLeaf;





    private RefUML_RedefinableElement refuml_redefinableelement;




    private List<RefUML_Classifier> refuml_classifiers;


    public RefUML_RedefinableElement(
        String isLeaf    ) {
        super(
        );
        this.isLeaf = isLeaf;
        this.refuml_classifiers = new ArrayList<>();
    }

    public RefUML_RedefinableElement(
        String isLeaf        ArrayList<RefUML_Classifier> refuml_classifiers    ) {
        this.isLeaf = isLeaf;
        this.refuml_classifiers = refuml_classifiers;
    }

    public String getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(String isLeaf) {
        this.isLeaf = isLeaf;
    }

    public RefUML_RedefinableElement getRefuml_redefinableelement() {
        return refuml_redefinableelement;
    }

    public void setRefuml_redefinableelement(RefUML_RedefinableElement refuml_redefinableelement) {
        this.refuml_redefinableelement = refuml_redefinableelement;
    }
    public List<RefUML_Classifier> getRefuml_classifiers() {
        return refuml_classifiers;
    }

    public void addRefuml_classifier(Refuml_classifier refuml_classifier) {
        this.refuml_classifiers.add(refuml_classifier);
    }

}