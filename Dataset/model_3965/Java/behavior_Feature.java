





import java.util.List;
import java.util.ArrayList;

public class behavior_Feature extends RedefinableElement {

    private boolean isStatic;





    private behavior_Classifier behavior_classifier;




    private List<behavior_Classifier> behavior_classifiers;


    public behavior_Feature(
        boolean isStatic    ) {
        super(
        );
        this.isStatic = isStatic;
        this.behavior_classifiers = new ArrayList<>();
    }

    public behavior_Feature(
        boolean isStatic        ArrayList<behavior_Classifier> behavior_classifiers    ) {
        this.isStatic = isStatic;
        this.behavior_classifiers = behavior_classifiers;
    }

    public boolean getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(boolean isStatic) {
        this.isStatic = isStatic;
    }

    public behavior_Classifier getBehavior_classifier() {
        return behavior_classifier;
    }

    public void setBehavior_classifier(behavior_Classifier behavior_classifier) {
        this.behavior_classifier = behavior_classifier;
    }
    public List<behavior_Classifier> getBehavior_classifiers() {
        return behavior_classifiers;
    }

    public void addBehavior_classifier(Behavior_classifier behavior_classifier) {
        this.behavior_classifiers.add(behavior_classifier);
    }

}