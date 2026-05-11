





import java.util.List;
import java.util.ArrayList;

public class simulink_Transition extends ContainableStateflowElement {

    private int executionOrder;
    private boolean isDefaultTransition;





    private simulink_Vertex simulink_vertex;




    private simulink_Vertex simulink_vertex;




    private List<simulink_Action> simulink_actions;




    private simulink_Vertex simulink_vertex;




    private simulink_Action simulink_action;




    private simulink_Vertex simulink_vertex;


    public simulink_Transition(
        int executionOrder,        boolean isDefaultTransition    ) {
        super(
        );
        this.executionOrder = executionOrder;
        this.isDefaultTransition = isDefaultTransition;
        this.simulink_actions = new ArrayList<>();
    }

    public simulink_Transition(
        int executionOrder,        boolean isDefaultTransition        ArrayList<simulink_Action> simulink_actions    ) {
        this.executionOrder = executionOrder;
        this.isDefaultTransition = isDefaultTransition;
        this.simulink_actions = simulink_actions;
    }

    public int getExecutionorder() {
        return executionOrder;
    }

    public void setExecutionorder(int executionOrder) {
        this.executionOrder = executionOrder;
    }
    public boolean getIsdefaulttransition() {
        return isDefaultTransition;
    }

    public void setIsdefaulttransition(boolean isDefaultTransition) {
        this.isDefaultTransition = isDefaultTransition;
    }

    public simulink_Vertex getSimulink_vertex() {
        return simulink_vertex;
    }

    public void setSimulink_vertex(simulink_Vertex simulink_vertex) {
        this.simulink_vertex = simulink_vertex;
    }
    public simulink_Vertex getSimulink_vertex() {
        return simulink_vertex;
    }

    public void setSimulink_vertex(simulink_Vertex simulink_vertex) {
        this.simulink_vertex = simulink_vertex;
    }
    public List<simulink_Action> getSimulink_actions() {
        return simulink_actions;
    }

    public void addSimulink_action(Simulink_action simulink_action) {
        this.simulink_actions.add(simulink_action);
    }
    public simulink_Vertex getSimulink_vertex() {
        return simulink_vertex;
    }

    public void setSimulink_vertex(simulink_Vertex simulink_vertex) {
        this.simulink_vertex = simulink_vertex;
    }
    public simulink_Action getSimulink_action() {
        return simulink_action;
    }

    public void setSimulink_action(simulink_Action simulink_action) {
        this.simulink_action = simulink_action;
    }
    public simulink_Vertex getSimulink_vertex() {
        return simulink_vertex;
    }

    public void setSimulink_vertex(simulink_Vertex simulink_vertex) {
        this.simulink_vertex = simulink_vertex;
    }

}