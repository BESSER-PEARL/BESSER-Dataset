





import java.util.List;
import java.util.ArrayList;

public class ClassesProv_Classifier extends Type, Namespace, RedefinableElement {

    private boolean isAbstract;
    private boolean isFinalSpecialization;





    private List<ClassesProv_NamedElement> classesprov_namedelements;




    private List<ClassesProv_Generalization> classesprov_generalizations;




    private ClassesProv_Generalization classesprov_generalization;




    private ClassesProv_RedefinableElement classesprov_redefinableelement;




    private ClassesProv_Classifier classesprov_classifier;




    private ClassesProv_Generalization classesprov_generalization;




    private ClassesProv_Classifier classesprov_classifier;


    public ClassesProv_Classifier(
        boolean isAbstract,        boolean isFinalSpecialization    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.isFinalSpecialization = isFinalSpecialization;
        this.classesprov_namedelements = new ArrayList<>();
        this.classesprov_generalizations = new ArrayList<>();
    }

    public ClassesProv_Classifier(
        boolean isAbstract,        boolean isFinalSpecialization        ArrayList<ClassesProv_NamedElement> classesprov_namedelements,        ArrayList<ClassesProv_Generalization> classesprov_generalizations    ) {
        this.isAbstract = isAbstract;
        this.isFinalSpecialization = isFinalSpecialization;
        this.classesprov_namedelements = classesprov_namedelements;
        this.classesprov_generalizations = classesprov_generalizations;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }
    public boolean getIsfinalspecialization() {
        return isFinalSpecialization;
    }

    public void setIsfinalspecialization(boolean isFinalSpecialization) {
        this.isFinalSpecialization = isFinalSpecialization;
    }

    public List<ClassesProv_NamedElement> getClassesprov_namedelements() {
        return classesprov_namedelements;
    }

    public void addClassesprov_namedelement(Classesprov_namedelement classesprov_namedelement) {
        this.classesprov_namedelements.add(classesprov_namedelement);
    }
    public List<ClassesProv_Generalization> getClassesprov_generalizations() {
        return classesprov_generalizations;
    }

    public void addClassesprov_generalization(Classesprov_generalization classesprov_generalization) {
        this.classesprov_generalizations.add(classesprov_generalization);
    }
    public ClassesProv_Generalization getClassesprov_generalization() {
        return classesprov_generalization;
    }

    public void setClassesprov_generalization(ClassesProv_Generalization classesprov_generalization) {
        this.classesprov_generalization = classesprov_generalization;
    }
    public ClassesProv_RedefinableElement getClassesprov_redefinableelement() {
        return classesprov_redefinableelement;
    }

    public void setClassesprov_redefinableelement(ClassesProv_RedefinableElement classesprov_redefinableelement) {
        this.classesprov_redefinableelement = classesprov_redefinableelement;
    }
    public ClassesProv_Classifier getClassesprov_classifier() {
        return classesprov_classifier;
    }

    public void setClassesprov_classifier(ClassesProv_Classifier classesprov_classifier) {
        this.classesprov_classifier = classesprov_classifier;
    }
    public ClassesProv_Generalization getClassesprov_generalization() {
        return classesprov_generalization;
    }

    public void setClassesprov_generalization(ClassesProv_Generalization classesprov_generalization) {
        this.classesprov_generalization = classesprov_generalization;
    }
    public ClassesProv_Classifier getClassesprov_classifier() {
        return classesprov_classifier;
    }

    public void setClassesprov_classifier(ClassesProv_Classifier classesprov_classifier) {
        this.classesprov_classifier = classesprov_classifier;
    }

}