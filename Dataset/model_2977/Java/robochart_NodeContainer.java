





import java.util.List;
import java.util.ArrayList;

public class robochart_NodeContainer  {






    private List<robochart_Transition> robochart_transitions;




    private List<robochart_Node> robochart_nodes;


    public robochart_NodeContainer(
    ) {
        this.robochart_transitions = new ArrayList<>();
        this.robochart_nodes = new ArrayList<>();
    }

    public robochart_NodeContainer(
        ArrayList<robochart_Transition> robochart_transitions,        ArrayList<robochart_Node> robochart_nodes    ) {
        this.robochart_transitions = robochart_transitions;
        this.robochart_nodes = robochart_nodes;
    }


    public List<robochart_Transition> getRobochart_transitions() {
        return robochart_transitions;
    }

    public void addRobochart_transition(Robochart_transition robochart_transition) {
        this.robochart_transitions.add(robochart_transition);
    }
    public List<robochart_Node> getRobochart_nodes() {
        return robochart_nodes;
    }

    public void addRobochart_node(Robochart_node robochart_node) {
        this.robochart_nodes.add(robochart_node);
    }

}