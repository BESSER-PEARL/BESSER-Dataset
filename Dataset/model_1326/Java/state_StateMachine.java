





import java.util.List;
import java.util.ArrayList;

public class state_StateMachine  {

    private String name;





    private List<state_Node> state_nodes;




    private List<state_Transition> state_transitions;


    public state_StateMachine(
        String name    ) {
        this.name = name;
        this.state_nodes = new ArrayList<>();
        this.state_transitions = new ArrayList<>();
    }

    public state_StateMachine(
        String name        ArrayList<state_Node> state_nodes,        ArrayList<state_Transition> state_transitions    ) {
        this.name = name;
        this.state_nodes = state_nodes;
        this.state_transitions = state_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<state_Node> getState_nodes() {
        return state_nodes;
    }

    public void addState_node(State_node state_node) {
        this.state_nodes.add(state_node);
    }
    public List<state_Transition> getState_transitions() {
        return state_transitions;
    }

    public void addState_transition(State_transition state_transition) {
        this.state_transitions.add(state_transition);
    }

}