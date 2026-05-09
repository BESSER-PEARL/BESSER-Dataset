





import java.util.List;
import java.util.ArrayList;

public class statemachine_Region  {

    private int priority;





    private statemachine_Statechart statemachine_statechart;




    private List<statemachine_Node> statemachine_nodes;




    private statemachine_State statemachine_state;


    public statemachine_Region(
        int priority    ) {
        this.priority = priority;
        this.statemachine_nodes = new ArrayList<>();
    }

    public statemachine_Region(
        int priority        ArrayList<statemachine_Node> statemachine_nodes    ) {
        this.priority = priority;
        this.statemachine_nodes = statemachine_nodes;
    }

    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public statemachine_Statechart getStatemachine_statechart() {
        return statemachine_statechart;
    }

    public void setStatemachine_statechart(statemachine_Statechart statemachine_statechart) {
        this.statemachine_statechart = statemachine_statechart;
    }
    public List<statemachine_Node> getStatemachine_nodes() {
        return statemachine_nodes;
    }

    public void addStatemachine_node(Statemachine_node statemachine_node) {
        this.statemachine_nodes.add(statemachine_node);
    }
    public statemachine_State getStatemachine_state() {
        return statemachine_state;
    }

    public void setStatemachine_state(statemachine_State statemachine_state) {
        this.statemachine_state = statemachine_state;
    }

}