





import java.util.List;
import java.util.ArrayList;

public class behavior_Classifier extends Namespace {

    private boolean isAbstract;





    private List<behavior_NamedElement> behavior_namedelements;




    private List<behavior_Classifier> behavior_classifiers;




    private behavior_RedefinableElement behavior_redefinableelement;




    private List<behavior_Classifier> behavior_classifiers;


    public behavior_Classifier(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.behavior_namedelements = new ArrayList<>();
        this.behavior_classifiers = new ArrayList<>();
        this.behavior_classifiers = new ArrayList<>();
    }

    public behavior_Classifier(
        boolean isAbstract        ArrayList<behavior_NamedElement> behavior_namedelements,        ArrayList<behavior_Classifier> behavior_classifiers,        ArrayList<behavior_Classifier> behavior_classifiers    ) {
        this.isAbstract = isAbstract;
        this.behavior_namedelements = behavior_namedelements;
        this.behavior_classifiers = behavior_classifiers;
        this.behavior_classifiers = behavior_classifiers;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<behavior_NamedElement> getBehavior_namedelements() {
        return behavior_namedelements;
    }

    public void addBehavior_namedelement(Behavior_namedelement behavior_namedelement) {
        this.behavior_namedelements.add(behavior_namedelement);
    }
    public List<behavior_Classifier> getBehavior_classifiers() {
        return behavior_classifiers;
    }

    public void addBehavior_classifier(Behavior_classifier behavior_classifier) {
        this.behavior_classifiers.add(behavior_classifier);
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

}