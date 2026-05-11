





import java.util.List;
import java.util.ArrayList;

public class StateMachine  {






    private behavioral_elements_state_machines_Transition behavioral_elements_state_machines_transition;




    private behavioral_elements_state_machines_State behavioral_elements_state_machines_state;




    private behavioral_elements_state_machines_SubmachineState behavioral_elements_state_machines_submachinestate;


    public StateMachine(
    ) {
    }



    public behavioral_elements_state_machines_Transition getBehavioral_elements_state_machines_transition() {
        return behavioral_elements_state_machines_transition;
    }

    public void setBehavioral_elements_state_machines_transition(behavioral_elements_state_machines_Transition behavioral_elements_state_machines_transition) {
        this.behavioral_elements_state_machines_transition = behavioral_elements_state_machines_transition;
    }
    public behavioral_elements_state_machines_State getBehavioral_elements_state_machines_state() {
        return behavioral_elements_state_machines_state;
    }

    public void setBehavioral_elements_state_machines_state(behavioral_elements_state_machines_State behavioral_elements_state_machines_state) {
        this.behavioral_elements_state_machines_state = behavioral_elements_state_machines_state;
    }
    public behavioral_elements_state_machines_SubmachineState getBehavioral_elements_state_machines_submachinestate() {
        return behavioral_elements_state_machines_submachinestate;
    }

    public void setBehavioral_elements_state_machines_submachinestate(behavioral_elements_state_machines_SubmachineState behavioral_elements_state_machines_submachinestate) {
        this.behavioral_elements_state_machines_submachinestate = behavioral_elements_state_machines_submachinestate;
    }

}