





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_RedefinableElement extends NamedElement {

    private String isLeaf;





    private List<RefOntoUML_RedefinableElement> refontouml_redefinableelements;




    private List<RefOntoUML_Classifier> refontouml_classifiers;


    public RefOntoUML_RedefinableElement(
        String isLeaf    ) {
        super(
        );
        this.isLeaf = isLeaf;
        this.refontouml_redefinableelements = new ArrayList<>();
        this.refontouml_classifiers = new ArrayList<>();
    }

    public RefOntoUML_RedefinableElement(
        String isLeaf        ArrayList<RefOntoUML_RedefinableElement> refontouml_redefinableelements,        ArrayList<RefOntoUML_Classifier> refontouml_classifiers    ) {
        this.isLeaf = isLeaf;
        this.refontouml_redefinableelements = refontouml_redefinableelements;
        this.refontouml_classifiers = refontouml_classifiers;
    }

    public String getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(String isLeaf) {
        this.isLeaf = isLeaf;
    }

    public List<RefOntoUML_RedefinableElement> getRefontouml_redefinableelements() {
        return refontouml_redefinableelements;
    }

    public void addRefontouml_redefinableelement(Refontouml_redefinableelement refontouml_redefinableelement) {
        this.refontouml_redefinableelements.add(refontouml_redefinableelement);
    }
    public List<RefOntoUML_Classifier> getRefontouml_classifiers() {
        return refontouml_classifiers;
    }

    public void addRefontouml_classifier(Refontouml_classifier refontouml_classifier) {
        this.refontouml_classifiers.add(refontouml_classifier);
    }

}