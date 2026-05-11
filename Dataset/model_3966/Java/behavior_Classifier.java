





import java.util.List;
import java.util.ArrayList;

public class behavior_Classifier extends Namespace {

    private boolean isAbstract;





    private behavior_Classifier behavior_classifier;




    private behavior_RedefinableElement behavior_redefinableelement;




    private List<behavior_Classifier> behavior_classifiers;




    private List<behavior_NamedElement> behavior_namedelements;


    public behavior_Classifier(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.behavior_classifiers = new ArrayList<>();
        this.behavior_namedelements = new ArrayList<>();
    }

    public behavior_Classifier(
        boolean isAbstract        ArrayList<behavior_Classifier> behavior_classifiers,        ArrayList<behavior_NamedElement> behavior_namedelements    ) {
        this.isAbstract = isAbstract;
        this.behavior_classifiers = behavior_classifiers;
        this.behavior_namedelements = behavior_namedelements;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public behavior_Classifier getBehavior_classifier() {
        return behavior_classifier;
    }

    public void setBehavior_classifier(behavior_Classifier behavior_classifier) {
        this.behavior_classifier = behavior_classifier;
    }
    public behavior_RedefinableElement getBehavior_redefinableelement() {
        return behavior_redefinableelement;
    }

    public void setBehavior_redefinableelement(behavior_RedefinableElement behavior_redefinableelement) {
        this.behavior_redefinableelement = behavior_redefinableelement;
    }
    public List<behavior_Classifier> getBehavior_classifiers() {
        return behavior_classifiers;
    }

    public void addBehavior_classifier(Behavior_classifier behavior_classifier) {
        this.behavior_classifiers.add(behavior_classifier);
    }
    public List<behavior_NamedElement> getBehavior_namedelements() {
        return behavior_namedelements;
    }

    public void addBehavior_namedelement(Behavior_namedelement behavior_namedelement) {
        this.behavior_namedelements.add(behavior_namedelement);
    }

}