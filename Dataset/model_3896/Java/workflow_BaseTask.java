





import java.util.List;
import java.util.ArrayList;

public class workflow_BaseTask extends AbstractTask {






    private workflow_Workflow workflow_workflow;




    private List<workflow_AbstractTask> workflow_abstracttasks;


    public workflow_BaseTask(
    ) {
        super(
        );
        this.workflow_abstracttasks = new ArrayList<>();
    }

    public workflow_BaseTask(
        ArrayList<workflow_AbstractTask> workflow_abstracttasks    ) {
        this.workflow_abstracttasks = workflow_abstracttasks;
    }


    public workflow_Workflow getWorkflow_workflow() {
        return workflow_workflow;
    }

    public void setWorkflow_workflow(workflow_Workflow workflow_workflow) {
        this.workflow_workflow = workflow_workflow;
    }
    public List<workflow_AbstractTask> getWorkflow_abstracttasks() {
        return workflow_abstracttasks;
    }

    public void addWorkflow_abstracttask(Workflow_abstracttask workflow_abstracttask) {
        this.workflow_abstracttasks.add(workflow_abstracttask);
    }

}