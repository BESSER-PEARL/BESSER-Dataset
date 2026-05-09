





import java.util.List;
import java.util.ArrayList;

public class state_Trigger extends NamedElement {






    private state_State state_state;




    private state_Transition state_transition;


    public state_Trigger(
    ) {
        super(
        );
    }



    public state_State getState_state() {
        return state_state;
    }

    public void setState_state(state_State state_state) {
        this.state_state = state_state;
    }
    public state_Transition getState_transition() {
        return state_transition;
    }

    public void setState_transition(state_Transition state_transition) {
        this.state_transition = state_transition;
    }

}