





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_Classifier extends Type, RedefinableElement, Namespace {

    private String isAbstract;





    private List<RefOntoUML_Classifier> refontouml_classifiers;




    private List<RefOntoUML_NamedElement> refontouml_namedelements;




    private RefOntoUML_Classifier refontouml_classifier;


    public RefOntoUML_Classifier(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.refontouml_classifiers = new ArrayList<>();
        this.refontouml_namedelements = new ArrayList<>();
    }

    public RefOntoUML_Classifier(
        String isAbstract        ArrayList<RefOntoUML_Classifier> refontouml_classifiers,        ArrayList<RefOntoUML_NamedElement> refontouml_namedelements    ) {
        this.isAbstract = isAbstract;
        this.refontouml_classifiers = refontouml_classifiers;
        this.refontouml_namedelements = refontouml_namedelements;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<RefOntoUML_Classifier> getRefontouml_classifiers() {
        return refontouml_classifiers;
    }

    public void addRefontouml_classifier(Refontouml_classifier refontouml_classifier) {
        this.refontouml_classifiers.add(refontouml_classifier);
    }
    public List<RefOntoUML_NamedElement> getRefontouml_namedelements() {
        return refontouml_namedelements;
    }

    public void addRefontouml_namedelement(Refontouml_namedelement refontouml_namedelement) {
        this.refontouml_namedelements.add(refontouml_namedelement);
    }
    public RefOntoUML_Classifier getRefontouml_classifier() {
        return refontouml_classifier;
    }

    public void setRefontouml_classifier(RefOntoUML_Classifier refontouml_classifier) {
        this.refontouml_classifier = refontouml_classifier;
    }

}