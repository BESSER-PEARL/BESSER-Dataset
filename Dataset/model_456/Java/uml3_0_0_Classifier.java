





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Classifier extends Namespace, Type, TemplateableElement, RedefinableElement {

    private String isAbstract;





    private uml3_0_0_ExceptionHandler uml3_0_0_exceptionhandler;




    private uml3_0_0_Classifier uml3_0_0_classifier;




    private List<uml3_0_0_NamedElement> uml3_0_0_namedelements;




    private List<uml3_0_0_Classifier> uml3_0_0_classifiers;


    public uml3_0_0_Classifier(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.uml3_0_0_namedelements = new ArrayList<>();
        this.uml3_0_0_classifiers = new ArrayList<>();
    }

    public uml3_0_0_Classifier(
        String isAbstract        ArrayList<uml3_0_0_NamedElement> uml3_0_0_namedelements,        ArrayList<uml3_0_0_Classifier> uml3_0_0_classifiers    ) {
        this.isAbstract = isAbstract;
        this.uml3_0_0_namedelements = uml3_0_0_namedelements;
        this.uml3_0_0_classifiers = uml3_0_0_classifiers;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public uml3_0_0_ExceptionHandler getUml3_0_0_exceptionhandler() {
        return uml3_0_0_exceptionhandler;
    }

    public void setUml3_0_0_exceptionhandler(uml3_0_0_ExceptionHandler uml3_0_0_exceptionhandler) {
        this.uml3_0_0_exceptionhandler = uml3_0_0_exceptionhandler;
    }
    public uml3_0_0_Classifier getUml3_0_0_classifier() {
        return uml3_0_0_classifier;
    }

    public void setUml3_0_0_classifier(uml3_0_0_Classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifier = uml3_0_0_classifier;
    }
    public List<uml3_0_0_NamedElement> getUml3_0_0_namedelements() {
        return uml3_0_0_namedelements;
    }

    public void addUml3_0_0_namedelement(Uml3_0_0_namedelement uml3_0_0_namedelement) {
        this.uml3_0_0_namedelements.add(uml3_0_0_namedelement);
    }
    public List<uml3_0_0_Classifier> getUml3_0_0_classifiers() {
        return uml3_0_0_classifiers;
    }

    public void addUml3_0_0_classifier(Uml3_0_0_classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifiers.add(uml3_0_0_classifier);
    }

}