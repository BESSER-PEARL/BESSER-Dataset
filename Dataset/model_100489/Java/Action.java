





import java.util.List;
import java.util.ArrayList;

public class Action  {






    private State_Machines_Transition state_machines_transition;




    private Common_Behavior_ActionSequence common_behavior_actionsequence;




    private Common_Behavior_Argument common_behavior_argument;


    public Action(
    ) {
    }



    public State_Machines_Transition getState_machines_transition() {
        return state_machines_transition;
    }

    public void setState_machines_transition(State_Machines_Transition state_machines_transition) {
        this.state_machines_transition = state_machines_transition;
    }
    public Common_Behavior_ActionSequence getCommon_behavior_actionsequence() {
        return common_behavior_actionsequence;
    }

    public void setCommon_behavior_actionsequence(Common_Behavior_ActionSequence common_behavior_actionsequence) {
        this.common_behavior_actionsequence = common_behavior_actionsequence;
    }
    public Common_Behavior_Argument getCommon_behavior_argument() {
        return common_behavior_argument;
    }

    public void setCommon_behavior_argument(Common_Behavior_Argument common_behavior_argument) {
        this.common_behavior_argument = common_behavior_argument;
    }

}