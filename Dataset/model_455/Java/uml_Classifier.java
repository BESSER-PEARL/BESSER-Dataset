





import java.util.List;
import java.util.ArrayList;

public class uml_Classifier extends Namespace, RedefinableElement, Type, TemplateableElement {

    private String isAbstract;





    private uml_Generalization uml_generalization;




    private List<uml_Generalization> uml_generalizations;




    private uml_ExceptionHandler uml_exceptionhandler;




    private List<uml_NamedElement> uml_namedelements;




    private uml_Generalization uml_generalization;




    private uml_InformationFlow uml_informationflow;




    private uml_Classifier uml_classifier;




    private uml_Classifier uml_classifier;


    public uml_Classifier(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.uml_generalizations = new ArrayList<>();
        this.uml_namedelements = new ArrayList<>();
    }

    public uml_Classifier(
        String isAbstract        ArrayList<uml_Generalization> uml_generalizations,        ArrayList<uml_NamedElement> uml_namedelements    ) {
        this.isAbstract = isAbstract;
        this.uml_generalizations = uml_generalizations;
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
    public List<uml_Generalization> getUml_generalizations() {
        return uml_generalizations;
    }

    public void addUml_generalization(Uml_generalization uml_generalization) {
        this.uml_generalizations.add(uml_generalization);
    }
    public uml_ExceptionHandler getUml_exceptionhandler() {
        return uml_exceptionhandler;
    }

    public void setUml_exceptionhandler(uml_ExceptionHandler uml_exceptionhandler) {
        this.uml_exceptionhandler = uml_exceptionhandler;
    }
    public List<uml_NamedElement> getUml_namedelements() {
        return uml_namedelements;
    }

    public void addUml_namedelement(Uml_namedelement uml_namedelement) {
        this.uml_namedelements.add(uml_namedelement);
    }
    public uml_Generalization getUml_generalization() {
        return uml_generalization;
    }

    public void setUml_generalization(uml_Generalization uml_generalization) {
        this.uml_generalization = uml_generalization;
    }
    public uml_InformationFlow getUml_informationflow() {
        return uml_informationflow;
    }

    public void setUml_informationflow(uml_InformationFlow uml_informationflow) {
        this.uml_informationflow = uml_informationflow;
    }
    public uml_Classifier getUml_classifier() {
        return uml_classifier;
    }

    public void setUml_classifier(uml_Classifier uml_classifier) {
        this.uml_classifier = uml_classifier;
    }
    public uml_Classifier getUml_classifier() {
        return uml_classifier;
    }

    public void setUml_classifier(uml_Classifier uml_classifier) {
        this.uml_classifier = uml_classifier;
    }

}