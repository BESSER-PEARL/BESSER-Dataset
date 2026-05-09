





import java.util.List;
import java.util.ArrayList;

public class uml_Classifier extends Type {

    private String isAbstract;





    private uml_Generalization uml_generalization;




    private List<uml_Classifier> uml_classifiers;




    private uml_Generalization uml_generalization;




    private uml_Classifier uml_classifier;




    private List<uml_NamedElement> uml_namedelements;


    public uml_Classifier(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.uml_classifiers = new ArrayList<>();
        this.uml_namedelements = new ArrayList<>();
    }

    public uml_Classifier(
        String isAbstract        ArrayList<uml_Classifier> uml_classifiers,        ArrayList<uml_NamedElement> uml_namedelements    ) {
        this.isAbstract = isAbstract;
        this.uml_classifiers = uml_classifiers;
        this.uml_namedelements = uml_namedelements;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public uml_Generalization getUml_generalization() {
        return uml_generalization;
    }

    public void setUml_generalization(uml_Generalization uml_generalization) {
        this.uml_generalization = uml_generalization;
    }
    public List<uml_Classifier> getUml_classifiers() {
        return uml_classifiers;
    }

    public void addUml_classifier(Uml_classifier uml_classifier) {
        this.uml_classifiers.add(uml_classifier);
    }
    public uml_Generalization getUml_generalization() {
        return uml_generalization;
    }

    public void setUml_generalization(uml_Generalization uml_generalization) {
        this.uml_generalization = uml_generalization;
    }
    public uml_Classifier getUml_classifier() {
        return uml_classifier;
    }

    public void setUml_classifier(uml_Classifier uml_classifier) {
        this.uml_classifier = uml_classifier;
    }
    public List<uml_NamedElement> getUml_namedelements() {
        return uml_namedelements;
    }

    public void addUml_namedelement(Uml_namedelement uml_namedelement) {
        this.uml_namedelements.add(uml_namedelement);
    }

}