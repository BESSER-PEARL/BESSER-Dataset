





import java.util.List;
import java.util.ArrayList;

public class Event  {






    private State_Machines_Transition state_machines_transition;




    private State_Machines_State state_machines_state;


    public Event(
    ) {
    }



    public State_Machines_Transition getState_machines_transition() {
        return state_machines_transition;
    }

    public void setState_machines_transition(State_Machines_Transition state_machines_transition) {
        this.state_machines_transition = state_machines_transition;
    }
    public State_Machines_State getState_machines_state() {
        return state_machines_state;
    }

    public void setState_machines_state(State_Machines_State state_machines_state) {
        this.state_machines_state = state_machines_state;
    }

}