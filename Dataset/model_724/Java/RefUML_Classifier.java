





import java.util.List;
import java.util.ArrayList;

public class RefUML_Classifier extends RedefinableElement, Type, Namespace {

    private String isAbstract;





    private RefUML_Classifier refuml_classifier;




    private List<RefUML_Classifier> refuml_classifiers;




    private List<RefUML_NamedElement> refuml_namedelements;


    public RefUML_Classifier(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.refuml_classifiers = new ArrayList<>();
        this.refuml_namedelements = new ArrayList<>();
    }

    public RefUML_Classifier(
        String isAbstract        ArrayList<RefUML_Classifier> refuml_classifiers,        ArrayList<RefUML_NamedElement> refuml_namedelements    ) {
        this.isAbstract = isAbstract;
        this.refuml_classifiers = refuml_classifiers;
        this.refuml_namedelements = refuml_namedelements;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public RefUML_Classifier getRefuml_classifier() {
        return refuml_classifier;
    }

    public void setRefuml_classifier(RefUML_Classifier refuml_classifier) {
        this.refuml_classifier = refuml_classifier;
    }
    public List<RefUML_Classifier> getRefuml_classifiers() {
        return refuml_classifiers;
    }

    public void addRefuml_classifier(Refuml_classifier refuml_classifier) {
        this.refuml_classifiers.add(refuml_classifier);
    }
    public List<RefUML_NamedElement> getRefuml_namedelements() {
        return refuml_namedelements;
    }

    public void addRefuml_namedelement(Refuml_namedelement refuml_namedelement) {
        this.refuml_namedelements.add(refuml_namedelement);
    }

}