





import java.util.List;
import java.util.ArrayList;

public class workflow_ProcessO extends ProcessAspect {






    private List<workflow_Role> workflow_roles;


    public workflow_ProcessO(
    ) {
        super(
        );
        this.workflow_roles = new ArrayList<>();
    }

    public workflow_ProcessO(
        ArrayList<workflow_Role> workflow_roles    ) {
        this.workflow_roles = workflow_roles;
    }


    public List<workflow_Role> getWorkflow_roles() {
        return workflow_roles;
    }

    public void addWorkflow_role(Workflow_role workflow_role) {
        this.workflow_roles.add(workflow_role);
    }

}