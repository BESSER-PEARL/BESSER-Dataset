





import java.util.List;
import java.util.ArrayList;

public class behavior_Behavior extends Class {






    private List<behavior_Behavior> behavior_behaviors;




    private behavior_BehavioralFeature behavior_behavioralfeature;




    private behavior_BehavioralFeature behavior_behavioralfeature;




    private behavior_Connector behavior_connector;


    public behavior_Behavior(
    ) {
        super(
        );
        this.behavior_behaviors = new ArrayList<>();
    }

    public behavior_Behavior(
        ArrayList<behavior_Behavior> behavior_behaviors    ) {
        this.behavior_behaviors = behavior_behaviors;
    }


    public List<behavior_Behavior> getBehavior_behaviors() {
        return behavior_behaviors;
    }

    public void addBehavior_behavior(Behavior_behavior behavior_behavior) {
        this.behavior_behaviors.add(behavior_behavior);
    }
    public behavior_BehavioralFeature getBehavior_behavioralfeature() {
        return behavior_behavioralfeature;
    }

    public void setBehavior_behavioralfeature(behavior_BehavioralFeature behavior_behavioralfeature) {
        this.behavior_behavioralfeature = behavior_behavioralfeature;
    }
    public behavior_BehavioralFeature getBehavior_behavioralfeature() {
        return behavior_behavioralfeature;
    }

    public void setBehavior_behavioralfeature(behavior_BehavioralFeature behavior_behavioralfeature) {
        this.behavior_behavioralfeature = behavior_behavioralfeature;
    }
    public behavior_Connector getBehavior_connector() {
        return behavior_connector;
    }

    public void setBehavior_connector(behavior_Connector behavior_connector) {
        this.behavior_connector = behavior_connector;
    }

}