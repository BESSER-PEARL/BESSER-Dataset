





import java.util.List;
import java.util.ArrayList;

public class workflow_ToState  {






    private workflow_StateTransition workflow_statetransition;




    private List<workflow_StateTransition> workflow_statetransitions;


    public workflow_ToState(
    ) {
        this.workflow_statetransitions = new ArrayList<>();
    }

    public workflow_ToState(
        ArrayList<workflow_StateTransition> workflow_statetransitions    ) {
        this.workflow_statetransitions = workflow_statetransitions;
    }


    public workflow_StateTransition getWorkflow_statetransition() {
        return workflow_statetransition;
    }

    public void setWorkflow_statetransition(workflow_StateTransition workflow_statetransition) {
        this.workflow_statetransition = workflow_statetransition;
    }
    public List<workflow_StateTransition> getWorkflow_statetransitions() {
        return workflow_statetransitions;
    }

    public void addWorkflow_statetransition(Workflow_statetransition workflow_statetransition) {
        this.workflow_statetransitions.add(workflow_statetransition);
    }

}