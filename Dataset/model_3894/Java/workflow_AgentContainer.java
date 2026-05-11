





import java.util.List;
import java.util.ArrayList;

public class workflow_AgentContainer extends RuntimeGlobalAspect {

    private String name;





    private List<workflow_Agent> workflow_agents;


    public workflow_AgentContainer(
        String name    ) {
        super(
        );
        this.name = name;
        this.workflow_agents = new ArrayList<>();
    }

    public workflow_AgentContainer(
        String name        ArrayList<workflow_Agent> workflow_agents    ) {
        this.name = name;
        this.workflow_agents = workflow_agents;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<workflow_Agent> getWorkflow_agents() {
        return workflow_agents;
    }

    public void addWorkflow_agent(Workflow_agent workflow_agent) {
        this.workflow_agents.add(workflow_agent);
    }

}