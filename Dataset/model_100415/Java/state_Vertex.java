





import java.util.List;
import java.util.ArrayList;

public class state_Vertex extends NamedElement {






    private state_Transition state_transition;




    private List<state_Transition> state_transitions;




    private state_Region state_region;




    private state_Transition state_transition;




    private List<state_Transition> state_transitions;


    public state_Vertex(
    ) {
        super(
        );
        this.state_transitions = new ArrayList<>();
        this.state_transitions = new ArrayList<>();
    }

    public state_Vertex(
        ArrayList<state_Transition> state_transitions,        ArrayList<state_Transition> state_transitions    ) {
        this.state_transitions = state_transitions;
        this.state_transitions = state_transitions;
    }


    public state_Transition getState_transition() {
        return state_transition;
    }

    public void setState_transition(state_Transition state_transition) {
        this.state_transition = state_transition;
    }
    public List<state_Transition> getState_transitions() {
        return state_transitions;
    }

    public void addState_transition(State_transition state_transition) {
        this.state_transitions.add(state_transition);
    }
    public state_Region getState_region() {
        return state_region;
    }

    public void setState_region(state_Region state_region) {
        this.state_region = state_region;
    }
    public state_Transition getState_transition() {
        return state_transition;
    }

    public void setState_transition(state_Transition state_transition) {
        this.state_transition = state_transition;
    }
    public List<state_Transition> getState_transitions() {
        return state_transitions;
    }

    public void addState_transition(State_transition state_transition) {
        this.state_transitions.add(state_transition);
    }

}