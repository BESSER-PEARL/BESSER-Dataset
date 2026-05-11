





import java.util.List;
import java.util.ArrayList;

public class workflow_CaseO extends CaseAspect {






    private List<workflow_Agent> workflow_agents;


    public workflow_CaseO(
    ) {
        super(
        );
        this.workflow_agents = new ArrayList<>();
    }

    public workflow_CaseO(
        ArrayList<workflow_Agent> workflow_agents    ) {
        this.workflow_agents = workflow_agents;
    }


    public List<workflow_Agent> getWorkflow_agents() {
        return workflow_agents;
    }

    public void addWorkflow_agent(Workflow_agent workflow_agent) {
        this.workflow_agents.add(workflow_agent);
    }

}