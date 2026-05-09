





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_RedefinableElement extends NamedElement {

    private String isLeaf;





    private List<RefOntoUML_Classifier> refontouml_classifiers;




    private RefOntoUML_RedefinableElement refontouml_redefinableelement;


    public RefOntoUML_RedefinableElement(
        String isLeaf    ) {
        super(
        );
        this.isLeaf = isLeaf;
        this.refontouml_classifiers = new ArrayList<>();
    }

    public RefOntoUML_RedefinableElement(
        String isLeaf        ArrayList<RefOntoUML_Classifier> refontouml_classifiers    ) {
        this.isLeaf = isLeaf;
        this.refontouml_classifiers = refontouml_classifiers;
    }

    public String getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(String isLeaf) {
        this.isLeaf = isLeaf;
    }

    public List<RefOntoUML_Classifier> getRefontouml_classifiers() {
        return refontouml_classifiers;
    }

    public void addRefontouml_classifier(Refontouml_classifier refontouml_classifier) {
        this.refontouml_classifiers.add(refontouml_classifier);
    }
    public RefOntoUML_RedefinableElement getRefontouml_redefinableelement() {
        return refontouml_redefinableelement;
    }

    public void setRefontouml_redefinableelement(RefOntoUML_RedefinableElement refontouml_redefinableelement) {
        this.refontouml_redefinableelement = refontouml_redefinableelement;
    }

}