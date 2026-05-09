





import java.util.List;
import java.util.ArrayList;

public class state_Region extends NamedElement {






    private List<state_Transition> state_transitions;




    private state_State state_state;




    private state_StateMachine state_statemachine;




    private state_StateMachine state_statemachine;




    private state_State state_state;




    private List<state_Vertex> state_vertexs;


    public state_Region(
    ) {
        super(
        );
        this.state_transitions = new ArrayList<>();
        this.state_vertexs = new ArrayList<>();
    }

    public state_Region(
        ArrayList<state_Transition> state_transitions,        ArrayList<state_Vertex> state_vertexs    ) {
        this.state_transitions = state_transitions;
        this.state_vertexs = state_vertexs;
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
    public state_StateMachine getState_statemachine() {
        return state_statemachine;
    }

    public void setState_statemachine(state_StateMachine state_statemachine) {
        this.state_statemachine = state_statemachine;
    }
    public state_StateMachine getState_statemachine() {
        return state_statemachine;
    }

    public void setState_statemachine(state_StateMachine state_statemachine) {
        this.state_statemachine = state_statemachine;
    }
    public state_State getState_state() {
        return state_state;
    }

    public void setState_state(state_State state_state) {
        this.state_state = state_state;
    }
    public List<state_Vertex> getState_vertexs() {
        return state_vertexs;
    }

    public void addState_vertex(State_vertex state_vertex) {
        this.state_vertexs.add(state_vertex);
    }

}