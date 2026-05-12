





import java.util.List;
import java.util.ArrayList;

public class state_Region extends NamedElement {






    private List<state_Transition> state_transitions;




    private state_State state_state;




    private state_State state_state;


    public state_Region(
    ) {
        super(
        );
        this.state_transitions = new ArrayList<>();
    }

    public state_Region(
        ArrayList<state_Transition> state_transitions    ) {
        this.state_transitions = state_transitions;
    }


    public List<state_Transition> getState_transitions() {
        return state_transitions;
    }

    public void addState_transition(State_transition state_transition) {
        this.state_transitions.add(state_transition);
    }
    public state_State getState_state() {
        return state_state;
    }

    public void setState_state(state_State state_state) {
        this.state_state = state_state;
    }
    public state_State getState_state() {
        return state_state;
    }

    public void setState_state(state_State state_state) {
        this.state_state = state_state;
    }

}