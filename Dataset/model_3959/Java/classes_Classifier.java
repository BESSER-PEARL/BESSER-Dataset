





import java.util.List;
import java.util.ArrayList;

public class classes_Classifier extends Type, Namespace {

    private boolean abstract;
    private boolean finalSpecialization;





    private classes_Generalization classes_generalization;




    private List<classes_Generalization> classes_generalizations;




    private classes_Generalization classes_generalization;




    private classes_RedefinableElement classes_redefinableelement;




    private classes_Classifier classes_classifier;




    private classes_InstanceSpecification classes_instancespecification;




    private List<classes_NamedElement> classes_namedelements;


    public classes_Classifier(
        boolean abstract,        boolean finalSpecialization    ) {
        super(
        );
        this.abstract = abstract;
        this.finalSpecialization = finalSpecialization;
        this.classes_generalizations = new ArrayList<>();
        this.classes_namedelements = new ArrayList<>();
    }

    public classes_Classifier(
        boolean abstract,        boolean finalSpecialization        ArrayList<classes_Generalization> classes_generalizations,        ArrayList<classes_NamedElement> classes_namedelements    ) {
        this.abstract = abstract;
        this.finalSpecialization = finalSpecialization;
        this.classes_generalizations = classes_generalizations;
        this.classes_namedelements = classes_namedelements;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getFinalspecialization() {
        return finalSpecialization;
    }

    public void setFinalspecialization(boolean finalSpecialization) {
        this.finalSpecialization = finalSpecialization;
    }

    public classes_Generalization getClasses_generalization() {
        return classes_generalization;
    }

    public void setClasses_generalization(classes_Generalization classes_generalization) {
        this.classes_generalization = classes_generalization;
    }
    public List<classes_Generalization> getClasses_generalizations() {
        return classes_generalizations;
    }

    public void addClasses_generalization(Classes_generalization classes_generalization) {
        this.classes_generalizations.add(classes_generalization);
    }
    public classes_Generalization getClasses_generalization() {
        return classes_generalization;
    }

    public void setClasses_generalization(classes_Generalization classes_generalization) {
        this.classes_generalization = classes_generalization;
    }
    public classes_RedefinableElement getClasses_redefinableelement() {
        return classes_redefinableelement;
    }

    public void setClasses_redefinableelement(classes_RedefinableElement classes_redefinableelement) {
        this.classes_redefinableelement = classes_redefinableelement;
    }
    public classes_Classifier getClasses_classifier() {
        return classes_classifier;
    }

    public void setClasses_classifier(classes_Classifier classes_classifier) {
        this.classes_classifier = classes_classifier;
    }
    public classes_InstanceSpecification getClasses_instancespecification() {
        return classes_instancespecification;
    }

    public void setClasses_instancespecification(classes_InstanceSpecification classes_instancespecification) {
        this.classes_instancespecification = classes_instancespecification;
    }
    public List<classes_NamedElement> getClasses_namedelements() {
        return classes_namedelements;
    }

    public void addClasses_namedelement(Classes_namedelement classes_namedelement) {
        this.classes_namedelements.add(classes_namedelement);
    }

}