





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Feature extends RedefinableElement {

    private boolean isStatic;





    private UML2WithID_Classifier uml2withid_classifier;




    private List<UML2WithID_Classifier> uml2withid_classifiers;


    public UML2WithID_Feature(
        boolean isStatic    ) {
        super(
        );
        this.isStatic = isStatic;
        this.uml2withid_classifiers = new ArrayList<>();
    }

    public UML2WithID_Feature(
        boolean isStatic        ArrayList<UML2WithID_Classifier> uml2withid_classifiers    ) {
        this.isStatic = isStatic;
        this.uml2withid_classifiers = uml2withid_classifiers;
    }

    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
    }

    public UML2WithID_Classifier getUml2withid_classifier() {
        return uml2withid_classifier;
    }

    public void setUml2withid_classifier(UML2WithID_Classifier uml2withid_classifier) {
        this.uml2withid_classifier = uml2withid_classifier;
    }
    public List<UML2WithID_Classifier> getUml2withid_classifiers() {
        return uml2withid_classifiers;
    }

    public void addUml2withid_classifier(Uml2withid_classifier uml2withid_classifier) {
        this.uml2withid_classifiers.add(uml2withid_classifier);
    }

}