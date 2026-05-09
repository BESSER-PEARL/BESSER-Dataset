





import java.util.List;
import java.util.ArrayList;

public class RefUML_RedefinableElement extends NamedElement {

    private String isLeaf;





    private List<RefUML_RedefinableElement> refuml_redefinableelements;




    private List<RefUML_Classifier> refuml_classifiers;


    public RefUML_RedefinableElement(
        String isLeaf    ) {
        super(
        );
        this.isLeaf = isLeaf;
        this.refuml_redefinableelements = new ArrayList<>();
        this.refuml_classifiers = new ArrayList<>();
    }

    public RefUML_RedefinableElement(
        String isLeaf        ArrayList<RefUML_RedefinableElement> refuml_redefinableelements,        ArrayList<RefUML_Classifier> refuml_classifiers    ) {
        this.isLeaf = isLeaf;
        this.refuml_redefinableelements = refuml_redefinableelements;
        this.refuml_classifiers = refuml_classifiers;
    }

    public String getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(String isLeaf) {
        this.isLeaf = isLeaf;
    }

    public List<RefUML_RedefinableElement> getRefuml_redefinableelements() {
        return refuml_redefinableelements;
    }

    public void addRefuml_redefinableelement(Refuml_redefinableelement refuml_redefinableelement) {
        this.refuml_redefinableelements.add(refuml_redefinableelement);
    }
    public List<RefUML_Classifier> getRefuml_classifiers() {
        return refuml_classifiers;
    }

    public void addRefuml_classifier(Refuml_classifier refuml_classifier) {
        this.refuml_classifiers.add(refuml_classifier);
    }

}