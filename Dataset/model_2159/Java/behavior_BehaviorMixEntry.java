





import java.util.List;
import java.util.ArrayList;

public class behavior_BehaviorMixEntry  {

    private String behaviorModelName;
    private float relativeFrequency;





    private behavior_BehaviorModelRelative behavior_behaviormodelrelative;




    private behavior_BehaviorMix behavior_behaviormix;


    public behavior_BehaviorMixEntry(
        String behaviorModelName,        float relativeFrequency    ) {
        this.behaviorModelName = behaviorModelName;
        this.relativeFrequency = relativeFrequency;
    }


    public String getBehaviormodelname() {
        return behaviorModelName;
    }

    public void setBehaviormodelname(String behaviorModelName) {
        this.behaviorModelName = behaviorModelName;
    }
    public float getRelativefrequency() {
        return relativeFrequency;
    }

    public void setRelativefrequency(float relativeFrequency) {
        this.relativeFrequency = relativeFrequency;
    }

    public behavior_BehaviorModelRelative getBehavior_behaviormodelrelative() {
        return behavior_behaviormodelrelative;
    }

    public void setBehavior_behaviormodelrelative(behavior_BehaviorModelRelative behavior_behaviormodelrelative) {
        this.behavior_behaviormodelrelative = behavior_behaviormodelrelative;
    }
    public behavior_BehaviorMix getBehavior_behaviormix() {
        return behavior_behaviormix;
    }

    public void setBehavior_behaviormix(behavior_BehaviorMix behavior_behaviormix) {
        this.behavior_behaviormix = behavior_behaviormix;
    }

}