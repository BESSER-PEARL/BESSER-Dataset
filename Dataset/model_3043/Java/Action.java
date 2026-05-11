





import java.util.List;
import java.util.ArrayList;

public class Action  {






    private behavioral_elements_collaborations_Message behavioral_elements_collaborations_message;




    private behavioral_elements_state_machines_Transition behavioral_elements_state_machines_transition;




    private behavioral_elements_common_behavior_Argument behavioral_elements_common_behavior_argument;




    private behavioral_elements_common_behavior_Stimulus behavioral_elements_common_behavior_stimulus;




    private behavioral_elements_common_behavior_ActionSequence behavioral_elements_common_behavior_actionsequence;


    public Action(
    ) {
    }



    public behavioral_elements_collaborations_Message getBehavioral_elements_collaborations_message() {
        return behavioral_elements_collaborations_message;
    }

    public void setBehavioral_elements_collaborations_message(behavioral_elements_collaborations_Message behavioral_elements_collaborations_message) {
        this.behavioral_elements_collaborations_message = behavioral_elements_collaborations_message;
    }
    public behavioral_elements_state_machines_Transition getBehavioral_elements_state_machines_transition() {
        return behavioral_elements_state_machines_transition;
    }

    public void setBehavioral_elements_state_machines_transition(behavioral_elements_state_machines_Transition behavioral_elements_state_machines_transition) {
        this.behavioral_elements_state_machines_transition = behavioral_elements_state_machines_transition;
    }
    public behavioral_elements_common_behavior_Argument getBehavioral_elements_common_behavior_argument() {
        return behavioral_elements_common_behavior_argument;
    }

    public void setBehavioral_elements_common_behavior_argument(behavioral_elements_common_behavior_Argument behavioral_elements_common_behavior_argument) {
        this.behavioral_elements_common_behavior_argument = behavioral_elements_common_behavior_argument;
    }
    public behavioral_elements_common_behavior_Stimulus getBehavioral_elements_common_behavior_stimulus() {
        return behavioral_elements_common_behavior_stimulus;
    }

    public void setBehavioral_elements_common_behavior_stimulus(behavioral_elements_common_behavior_Stimulus behavioral_elements_common_behavior_stimulus) {
        this.behavioral_elements_common_behavior_stimulus = behavioral_elements_common_behavior_stimulus;
    }
    public behavioral_elements_common_behavior_ActionSequence getBehavioral_elements_common_behavior_actionsequence() {
        return behavioral_elements_common_behavior_actionsequence;
    }

    public void setBehavioral_elements_common_behavior_actionsequence(behavioral_elements_common_behavior_ActionSequence behavioral_elements_common_behavior_actionsequence) {
        this.behavioral_elements_common_behavior_actionsequence = behavioral_elements_common_behavior_actionsequence;
    }

}