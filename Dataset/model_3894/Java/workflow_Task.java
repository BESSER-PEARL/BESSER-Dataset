





import java.util.List;
import java.util.ArrayList;

public class workflow_Task  {

    private String name;





    private workflow_Process workflow_process;




    private workflow_Activity workflow_activity;


    public workflow_Task(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public workflow_Process getWorkflow_process() {
        return workflow_process;
    }

    public void setWorkflow_process(workflow_Process workflow_process) {
        this.workflow_process = workflow_process;
    }
    public workflow_Activity getWorkflow_activity() {
        return workflow_activity;
    }

    public void setWorkflow_activity(workflow_Activity workflow_activity) {
        this.workflow_activity = workflow_activity;
    }

}