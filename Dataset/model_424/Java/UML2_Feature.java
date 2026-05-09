





import java.util.List;
import java.util.ArrayList;

public class UML2_Feature extends RedefinableElement {

    private boolean isStatic;





    private UML2_Classifier uml2_classifier;




    private List<UML2_Classifier> uml2_classifiers;


    public UML2_Feature(
        boolean isStatic    ) {
        super(
        );
        this.isStatic = isStatic;
        this.uml2_classifiers = new ArrayList<>();
    }

    public UML2_Feature(
        boolean isStatic        ArrayList<UML2_Classifier> uml2_classifiers    ) {
        this.isStatic = isStatic;
        this.uml2_classifiers = uml2_classifiers;
    }

    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
    }

    public UML2_Classifier getUml2_classifier() {
        return uml2_classifier;
    }

    public void setUml2_classifier(UML2_Classifier uml2_classifier) {
        this.uml2_classifier = uml2_classifier;
    }
    public List<UML2_Classifier> getUml2_classifiers() {
        return uml2_classifiers;
    }

    public void addUml2_classifier(Uml2_classifier uml2_classifier) {
        this.uml2_classifiers.add(uml2_classifier);
    }

}