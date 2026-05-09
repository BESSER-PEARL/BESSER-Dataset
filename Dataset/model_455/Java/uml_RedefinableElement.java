





import java.util.List;
import java.util.ArrayList;

public class uml_RedefinableElement extends NamedElement {

    private String isLeaf;





    private uml_RedefinableElement uml_redefinableelement;




    private List<uml_Classifier> uml_classifiers;


    public uml_RedefinableElement(
        String isLeaf    ) {
        super(
        );
        this.isLeaf = isLeaf;
        this.uml_classifiers = new ArrayList<>();
    }

    public uml_RedefinableElement(
        String isLeaf        ArrayList<uml_Classifier> uml_classifiers    ) {
        this.isLeaf = isLeaf;
        this.uml_classifiers = uml_classifiers;
    }

    public String getIsleaf() {
        return isLeaf;
    }

    public void setIsleaf(String isLeaf) {
        this.isLeaf = isLeaf;
    }

    public uml_RedefinableElement getUml_redefinableelement() {
        return uml_redefinableelement;
    }

    public void setUml_redefinableelement(uml_RedefinableElement uml_redefinableelement) {
        this.uml_redefinableelement = uml_redefinableelement;
    }
    public List<uml_Classifier> getUml_classifiers() {
        return uml_classifiers;
    }

    public void addUml_classifier(Uml_classifier uml_classifier) {
        this.uml_classifiers.add(uml_classifier);
    }

}