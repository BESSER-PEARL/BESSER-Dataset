





import java.util.List;
import java.util.ArrayList;

public class workflow_WorkflowNode extends WorkflowElement {

    private boolean isFinish;
    private boolean isStart;





    private workflow_Workflow workflow_workflow;




    private workflow_Workflow workflow_workflow;


    public workflow_WorkflowNode(
        boolean isFinish,        boolean isStart    ) {
        super(
        );
        this.isFinish = isFinish;
        this.isStart = isStart;
    }


    public boolean getIsfinish() {
        return isFinish;
    }

    public void setIsfinish(boolean isFinish) {
        this.isFinish = isFinish;
    }
    public boolean getIsstart() {
        return isStart;
    }

    public void setIsstart(boolean isStart) {
        this.isStart = isStart;
    }

    public workflow_Workflow getWorkflow_workflow() {
        return workflow_workflow;
    }

    public void setWorkflow_workflow(workflow_Workflow workflow_workflow) {
        this.workflow_workflow = workflow_workflow;
    }
    public workflow_Workflow getWorkflow_workflow() {
        return workflow_workflow;
    }

    public void setWorkflow_workflow(workflow_Workflow workflow_workflow) {
        this.workflow_workflow = workflow_workflow;
    }

}