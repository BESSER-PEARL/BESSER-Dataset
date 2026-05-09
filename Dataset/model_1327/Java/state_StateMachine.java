





import java.util.List;
import java.util.ArrayList;

public class state_StateMachine  {

    private String name;





    private List<state_Node> state_nodes;


    public state_StateMachine(
        String name    ) {
        this.name = name;
        this.state_nodes = new ArrayList<>();
    }

    public state_StateMachine(
        String name        ArrayList<state_Node> state_nodes    ) {
        this.name = name;
        this.state_nodes = state_nodes;
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

}