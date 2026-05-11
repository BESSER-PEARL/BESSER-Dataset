





import java.util.List;
import java.util.ArrayList;

public class workflow_Program  {

    private int exec_order;
    private String name_exec;
    private String description;





    private List<workflow_Parameter> workflow_parameters;




    private workflow_SimpleCommand workflow_simplecommand;


    public workflow_Program(
        int exec_order,        String name_exec,        String description    ) {
        this.exec_order = exec_order;
        this.name_exec = name_exec;
        this.description = description;
        this.workflow_parameters = new ArrayList<>();
    }

    public workflow_Program(
        int exec_order,        String name_exec,        String description        ArrayList<workflow_Parameter> workflow_parameters    ) {
        this.exec_order = exec_order;
        this.name_exec = name_exec;
        this.description = description;
        this.workflow_parameters = workflow_parameters;
    }

    public int getExec_order() {
        return exec_order;
    }

    public void setExec_order(int exec_order) {
        this.exec_order = exec_order;
    }
    public String getName_exec() {
        return name_exec;
    }

    public void setName_exec(String name_exec) {
        this.name_exec = name_exec;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<workflow_Parameter> getWorkflow_parameters() {
        return workflow_parameters;
    }

    public void addWorkflow_parameter(Workflow_parameter workflow_parameter) {
        this.workflow_parameters.add(workflow_parameter);
    }
    public workflow_SimpleCommand getWorkflow_simplecommand() {
        return workflow_simplecommand;
    }

    public void setWorkflow_simplecommand(workflow_SimpleCommand workflow_simplecommand) {
        this.workflow_simplecommand = workflow_simplecommand;
    }

}