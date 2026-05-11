





import java.util.List;
import java.util.ArrayList;

public class workflow_Agent  {

    private String username;
    private String name;
    private String password;





    private List<workflow_ActivityO> workflow_activityos;




    private List<workflow_Role> workflow_roles;




    private workflow_ActivityO workflow_activityo;




    private List<workflow_Role> workflow_roles;


    public workflow_Agent(
        String username,        String name,        String password    ) {
        this.username = username;
        this.name = name;
        this.password = password;
        this.workflow_activityos = new ArrayList<>();
        this.workflow_roles = new ArrayList<>();
        this.workflow_roles = new ArrayList<>();
    }

    public workflow_Agent(
        String username,        String name,        String password        ArrayList<workflow_ActivityO> workflow_activityos,        ArrayList<workflow_Role> workflow_roles,        ArrayList<workflow_Role> workflow_roles    ) {
        this.username = username;
        this.name = name;
        this.password = password;
        this.workflow_activityos = workflow_activityos;
        this.workflow_roles = workflow_roles;
        this.workflow_roles = workflow_roles;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public List<workflow_ActivityO> getWorkflow_activityos() {
        return workflow_activityos;
    }

    public void addWorkflow_activityo(Workflow_activityo workflow_activityo) {
        this.workflow_activityos.add(workflow_activityo);
    }
    public List<workflow_Role> getWorkflow_roles() {
        return workflow_roles;
    }

    public void addWorkflow_role(Workflow_role workflow_role) {
        this.workflow_roles.add(workflow_role);
    }
    public workflow_ActivityO getWorkflow_activityo() {
        return workflow_activityo;
    }

    public void setWorkflow_activityo(workflow_ActivityO workflow_activityo) {
        this.workflow_activityo = workflow_activityo;
    }
    public List<workflow_Role> getWorkflow_roles() {
        return workflow_roles;
    }

    public void addWorkflow_role(Workflow_role workflow_role) {
        this.workflow_roles.add(workflow_role);
    }

}