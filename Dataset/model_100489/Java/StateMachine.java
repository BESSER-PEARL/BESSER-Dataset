





import java.util.List;
import java.util.ArrayList;

public class StateMachine  {






    private State_Machines_Transition state_machines_transition;




    private State_Machines_SubmachineState state_machines_submachinestate;


    public StateMachine(
    ) {
    }



    public State_Machines_Transition getState_machines_transition() {
        return state_machines_transition;
    }

    public void setState_machines_transition(State_Machines_Transition state_machines_transition) {
        this.state_machines_transition = state_machines_transition;
    }
    public State_Machines_SubmachineState getState_machines_submachinestate() {
        return state_machines_submachinestate;
    }

    public void setState_machines_submachinestate(State_Machines_SubmachineState state_machines_submachinestate) {
        this.state_machines_submachinestate = state_machines_submachinestate;
    }

}