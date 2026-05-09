





import java.util.List;
import java.util.ArrayList;

public class RefUML_Classifier extends Type, RedefinableElement, Namespace {

    private String isAbstract;





    private List<RefUML_Classifier> refuml_classifiers;




    private RefUML_Classifier refuml_classifier;


    public RefUML_Classifier(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.refuml_classifiers = new ArrayList<>();
    }

    public RefUML_Classifier(
        String isAbstract        ArrayList<RefUML_Classifier> refuml_classifiers    ) {
        this.isAbstract = isAbstract;
        this.refuml_classifiers = refuml_classifiers;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
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