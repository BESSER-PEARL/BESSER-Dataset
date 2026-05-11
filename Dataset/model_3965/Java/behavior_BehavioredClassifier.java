





import java.util.List;
import java.util.ArrayList;

public class behavior_BehavioredClassifier extends Classifier {






    private behavior_Lifeline behavior_lifeline;




    private List<behavior_Behavior> behavior_behaviors;




    private behavior_Behavior behavior_behavior;




    private behavior_Lifeline behavior_lifeline;




    private behavior_Behavior behavior_behavior;


    public behavior_BehavioredClassifier(
    ) {
        super(
        );
        this.behavior_behaviors = new ArrayList<>();
    }

    public behavior_BehavioredClassifier(
        ArrayList<behavior_Behavior> behavior_behaviors    ) {
        this.behavior_behaviors = behavior_behaviors;
    }


    public behavior_Lifeline getBehavior_lifeline() {
        return behavior_lifeline;
    }

    public void setBehavior_lifeline(behavior_Lifeline behavior_lifeline) {
        this.behavior_lifeline = behavior_lifeline;
    }
    public List<behavior_Behavior> getBehavior_behaviors() {
        return behavior_behaviors;
    }

    public void addBehavior_behavior(Behavior_behavior behavior_behavior) {
        this.behavior_behaviors.add(behavior_behavior);
    }
    public behavior_Behavior getBehavior_behavior() {
        return behavior_behavior;
    }

    public void setBehavior_behavior(behavior_Behavior behavior_behavior) {
        this.behavior_behavior = behavior_behavior;
    }
    public behavior_Lifeline getBehavior_lifeline() {
        return behavior_lifeline;
    }

    public void setBehavior_lifeline(behavior_Lifeline behavior_lifeline) {
        this.behavior_lifeline = behavior_lifeline;
    }
    public behavior_Behavior getBehavior_behavior() {
        return behavior_behavior;
    }

    public void setBehavior_behavior(behavior_Behavior behavior_behavior) {
        this.behavior_behavior = behavior_behavior;
    }

}