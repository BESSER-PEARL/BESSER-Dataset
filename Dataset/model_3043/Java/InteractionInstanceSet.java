





import java.util.List;
import java.util.ArrayList;

public class InteractionInstanceSet  {






    private behavioral_elements_common_behavior_Stimulus behavioral_elements_common_behavior_stimulus;




    private behavioral_elements_collaborations_CollaborationInstanceSet behavioral_elements_collaborations_collaborationinstanceset;




    private behavioral_elements_collaborations_Interaction behavioral_elements_collaborations_interaction;


    public InteractionInstanceSet(
    ) {
    }



    public behavioral_elements_common_behavior_Stimulus getBehavioral_elements_common_behavior_stimulus() {
        return behavioral_elements_common_behavior_stimulus;
    }

    public void setBehavioral_elements_common_behavior_stimulus(behavioral_elements_common_behavior_Stimulus behavioral_elements_common_behavior_stimulus) {
        this.behavioral_elements_common_behavior_stimulus = behavioral_elements_common_behavior_stimulus;
    }
    public behavioral_elements_collaborations_CollaborationInstanceSet getBehavioral_elements_collaborations_collaborationinstanceset() {
        return behavioral_elements_collaborations_collaborationinstanceset;
    }

    public void setBehavioral_elements_collaborations_collaborationinstanceset(behavioral_elements_collaborations_CollaborationInstanceSet behavioral_elements_collaborations_collaborationinstanceset) {
        this.behavioral_elements_collaborations_collaborationinstanceset = behavioral_elements_collaborations_collaborationinstanceset;
    }
    public behavioral_elements_collaborations_Interaction getBehavioral_elements_collaborations_interaction() {
        return behavioral_elements_collaborations_interaction;
    }

    public void setBehavioral_elements_collaborations_interaction(behavioral_elements_collaborations_Interaction behavioral_elements_collaborations_interaction) {
        this.behavioral_elements_collaborations_interaction = behavioral_elements_collaborations_interaction;
    }

}