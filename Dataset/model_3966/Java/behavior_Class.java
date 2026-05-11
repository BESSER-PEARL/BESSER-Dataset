





import java.util.List;
import java.util.ArrayList;

public class behavior_Class extends BehavioredClassifier {






    private List<behavior_Classifier> behavior_classifiers;


    public behavior_Class(
    ) {
        super(
        );
        this.behavior_classifiers = new ArrayList<>();
    }

    public behavior_Class(
        ArrayList<behavior_Classifier> behavior_classifiers    ) {
        this.behavior_classifiers = behavior_classifiers;
    }


    public List<behavior_Classifier> getBehavior_classifiers() {
        return behavior_classifiers;
    }

    public void addBehavior_classifier(Behavior_classifier behavior_classifier) {
        this.behavior_classifiers.add(behavior_classifier);
    }

}