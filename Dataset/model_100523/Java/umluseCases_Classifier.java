





import java.util.List;
import java.util.ArrayList;

public class umluseCases_Classifier extends Type, TemplateableElement, RedefinableElement, Namespace {

    private String isAbstract;





    private umluseCases_RedefinableElement umlusecases_redefinableelement;




    private List<umluseCases_Classifier> umlusecases_classifiers;




    private List<umluseCases_Classifier> umlusecases_classifiers;




    private List<umluseCases_NamedElement> umlusecases_namedelements;


    public umluseCases_Classifier(
        String isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.umlusecases_classifiers = new ArrayList<>();
        this.umlusecases_classifiers = new ArrayList<>();
        this.umlusecases_namedelements = new ArrayList<>();
    }

    public umluseCases_Classifier(
        String isAbstract        ArrayList<umluseCases_Classifier> umlusecases_classifiers,        ArrayList<umluseCases_Classifier> umlusecases_classifiers,        ArrayList<umluseCases_NamedElement> umlusecases_namedelements    ) {
        this.isAbstract = isAbstract;
        this.umlusecases_classifiers = umlusecases_classifiers;
        this.umlusecases_classifiers = umlusecases_classifiers;
        this.umlusecases_namedelements = umlusecases_namedelements;
    }

    public String getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(String isAbstract) {
        this.isAbstract = isAbstract;
    }

    public umluseCases_RedefinableElement getUmlusecases_redefinableelement() {
        return umlusecases_redefinableelement;
    }

    public void setUmlusecases_redefinableelement(umluseCases_RedefinableElement umlusecases_redefinableelement) {
        this.umlusecases_redefinableelement = umlusecases_redefinableelement;
    }
    public List<umluseCases_Classifier> getUmlusecases_classifiers() {
        return umlusecases_classifiers;
    }

    public void addUmlusecases_classifier(Umlusecases_classifier umlusecases_classifier) {
        this.umlusecases_classifiers.add(umlusecases_classifier);
    }
    public List<umluseCases_Classifier> getUmlusecases_classifiers() {
        return umlusecases_classifiers;
    }

    public void addUmlusecases_classifier(Umlusecases_classifier umlusecases_classifier) {
        this.umlusecases_classifiers.add(umlusecases_classifier);
    }
    public List<umluseCases_NamedElement> getUmlusecases_namedelements() {
        return umlusecases_namedelements;
    }

    public void addUmlusecases_namedelement(Umlusecases_namedelement umlusecases_namedelement) {
        this.umlusecases_namedelements.add(umlusecases_namedelement);
    }

}