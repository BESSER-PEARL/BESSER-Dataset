





import java.util.List;
import java.util.ArrayList;

public class workflow_Organisation extends GlobalAspect {

    private String name;





    private List<workflow_Role> workflow_roles;


    public workflow_Organisation(
        String name    ) {
        super(
        );
        this.name = name;
        this.workflow_roles = new ArrayList<>();
    }

    public workflow_Organisation(
        String name        ArrayList<workflow_Role> workflow_roles    ) {
        this.name = name;
        this.workflow_roles = workflow_roles;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<workflow_Role> getWorkflow_roles() {
        return workflow_roles;
    }

    public void addWorkflow_role(Workflow_role workflow_role) {
        this.workflow_roles.add(workflow_role);
    }

}