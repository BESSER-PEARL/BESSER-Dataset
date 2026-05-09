





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Classifier extends Namespace, Type, RedefinableElement {

    private boolean isAbstract;
    private boolean isFinalSpecialization;





    private List<CompleteDSLPckg_NamedElement> completedslpckg_namedelements;




    private CompleteDSLPckg_Generalization completedslpckg_generalization;




    private List<CompleteDSLPckg_Classifier> completedslpckg_classifiers;




    private CompleteDSLPckg_CollaborationUse completedslpckg_collaborationuse;




    private List<CompleteDSLPckg_Generalization> completedslpckg_generalizations;




    private CompleteDSLPckg_Generalization completedslpckg_generalization;




    private CompleteDSLPckg_Action completedslpckg_action;




    private List<CompleteDSLPckg_CollaborationUse> completedslpckg_collaborationuses;




    private CompleteDSLPckg_RedefinableElement completedslpckg_redefinableelement;




    private CompleteDSLPckg_ExceptionHandler completedslpckg_exceptionhandler;




    private List<CompleteDSLPckg_Classifier> completedslpckg_classifiers;


    public CompleteDSLPckg_Classifier(
        boolean isAbstract,        boolean isFinalSpecialization    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.isFinalSpecialization = isFinalSpecialization;
        this.completedslpckg_namedelements = new ArrayList<>();
        this.completedslpckg_classifiers = new ArrayList<>();
        this.completedslpckg_generalizations = new ArrayList<>();
        this.completedslpckg_collaborationuses = new ArrayList<>();
        this.completedslpckg_classifiers = new ArrayList<>();
    }

    public CompleteDSLPckg_Classifier(
        boolean isAbstract,        boolean isFinalSpecialization        ArrayList<CompleteDSLPckg_NamedElement> completedslpckg_namedelements,        ArrayList<CompleteDSLPckg_Classifier> completedslpckg_classifiers,        ArrayList<CompleteDSLPckg_Generalization> completedslpckg_generalizations,        ArrayList<CompleteDSLPckg_CollaborationUse> completedslpckg_collaborationuses,        ArrayList<CompleteDSLPckg_Classifier> completedslpckg_classifiers    ) {
        this.isAbstract = isAbstract;
        this.isFinalSpecialization = isFinalSpecialization;
        this.completedslpckg_namedelements = completedslpckg_namedelements;
        this.completedslpckg_classifiers = completedslpckg_classifiers;
        this.completedslpckg_generalizations = completedslpckg_generalizations;
        this.completedslpckg_collaborationuses = completedslpckg_collaborationuses;
        this.completedslpckg_classifiers = completedslpckg_classifiers;
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

    public List<CompleteDSLPckg_NamedElement> getCompletedslpckg_namedelements() {
        return completedslpckg_namedelements;
    }

    public void addCompletedslpckg_namedelement(Completedslpckg_namedelement completedslpckg_namedelement) {
        this.completedslpckg_namedelements.add(completedslpckg_namedelement);
    }
    public CompleteDSLPckg_Generalization getCompletedslpckg_generalization() {
        return completedslpckg_generalization;
    }

    public void setCompletedslpckg_generalization(CompleteDSLPckg_Generalization completedslpckg_generalization) {
        this.completedslpckg_generalization = completedslpckg_generalization;
    }
    public List<CompleteDSLPckg_Classifier> getCompletedslpckg_classifiers() {
        return completedslpckg_classifiers;
    }

    public void addCompletedslpckg_classifier(Completedslpckg_classifier completedslpckg_classifier) {
        this.completedslpckg_classifiers.add(completedslpckg_classifier);
    }
    public CompleteDSLPckg_CollaborationUse getCompletedslpckg_collaborationuse() {
        return completedslpckg_collaborationuse;
    }

    public void setCompletedslpckg_collaborationuse(CompleteDSLPckg_CollaborationUse completedslpckg_collaborationuse) {
        this.completedslpckg_collaborationuse = completedslpckg_collaborationuse;
    }
    public List<CompleteDSLPckg_Generalization> getCompletedslpckg_generalizations() {
        return completedslpckg_generalizations;
    }

    public void addCompletedslpckg_generalization(Completedslpckg_generalization completedslpckg_generalization) {
        this.completedslpckg_generalizations.add(completedslpckg_generalization);
    }
    public CompleteDSLPckg_Generalization getCompletedslpckg_generalization() {
        return completedslpckg_generalization;
    }

    public void setCompletedslpckg_generalization(CompleteDSLPckg_Generalization completedslpckg_generalization) {
        this.completedslpckg_generalization = completedslpckg_generalization;
    }
    public CompleteDSLPckg_Action getCompletedslpckg_action() {
        return completedslpckg_action;
    }

    public void setCompletedslpckg_action(CompleteDSLPckg_Action completedslpckg_action) {
        this.completedslpckg_action = completedslpckg_action;
    }
    public List<CompleteDSLPckg_CollaborationUse> getCompletedslpckg_collaborationuses() {
        return completedslpckg_collaborationuses;
    }

    public void addCompletedslpckg_collaborationuse(Completedslpckg_collaborationuse completedslpckg_collaborationuse) {
        this.completedslpckg_collaborationuses.add(completedslpckg_collaborationuse);
    }
    public CompleteDSLPckg_RedefinableElement getCompletedslpckg_redefinableelement() {
        return completedslpckg_redefinableelement;
    }

    public void setCompletedslpckg_redefinableelement(CompleteDSLPckg_RedefinableElement completedslpckg_redefinableelement) {
        this.completedslpckg_redefinableelement = completedslpckg_redefinableelement;
    }
    public CompleteDSLPckg_ExceptionHandler getCompletedslpckg_exceptionhandler() {
        return completedslpckg_exceptionhandler;
    }

    public void setCompletedslpckg_exceptionhandler(CompleteDSLPckg_ExceptionHandler completedslpckg_exceptionhandler) {
        this.completedslpckg_exceptionhandler = completedslpckg_exceptionhandler;
    }
    public List<CompleteDSLPckg_Classifier> getCompletedslpckg_classifiers() {
        return completedslpckg_classifiers;
    }

    public void addCompletedslpckg_classifier(Completedslpckg_classifier completedslpckg_classifier) {
        this.completedslpckg_classifiers.add(completedslpckg_classifier);
    }

}