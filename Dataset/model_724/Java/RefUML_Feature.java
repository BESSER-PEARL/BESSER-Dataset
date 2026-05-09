





import java.util.List;
import java.util.ArrayList;

public class RefUML_Feature extends RedefinableElement {

    private String isStatic;





    private List<RefUML_Classifier> refuml_classifiers;




    private RefUML_Classifier refuml_classifier;


    public RefUML_Feature(
        String isStatic    ) {
        super(
        );
        this.isStatic = isStatic;
        this.refuml_classifiers = new ArrayList<>();
    }

    public RefUML_Feature(
        String isStatic        ArrayList<RefUML_Classifier> refuml_classifiers    ) {
        this.isStatic = isStatic;
        this.refuml_classifiers = refuml_classifiers;
    }

    public String getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(String isStatic) {
        this.isStatic = isStatic;
    }

    public List<RefUML_Classifier> getRefuml_classifiers() {
        return refuml_classifiers;
    }

    public void addRefuml_classifier(Refuml_classifier refuml_classifier) {
        this.refuml_classifiers.add(refuml_classifier);
    }
    public RefUML_Classifier getRefuml_classifier() {
        return refuml_classifier;
    }

    public void setRefuml_classifier(RefUML_Classifier refuml_classifier) {
        this.refuml_classifier = refuml_classifier;
    }

}