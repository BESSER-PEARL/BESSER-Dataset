





import java.util.List;
import java.util.ArrayList;

public class workflow_WorkflowNode extends WorkflowElement {

    private boolean isStart;
    private boolean isFinish;





    private workflow_InputPort workflow_inputport;




    private List<workflow_OutputPort> workflow_outputports;




    private List<workflow_InputPort> workflow_inputports;




    private workflow_Workflow workflow_workflow;




    private workflow_OutputPort workflow_outputport;




    private workflow_Workflow workflow_workflow;


    public workflow_WorkflowNode(
        boolean isStart,        boolean isFinish    ) {
        super(
        );
        this.isStart = isStart;
        this.isFinish = isFinish;
        this.workflow_outputports = new ArrayList<>();
        this.workflow_inputports = new ArrayList<>();
    }

    public workflow_WorkflowNode(
        boolean isStart,        boolean isFinish        ArrayList<workflow_OutputPort> workflow_outputports,        ArrayList<workflow_InputPort> workflow_inputports    ) {
        this.isStart = isStart;
        this.isFinish = isFinish;
        this.workflow_outputports = workflow_outputports;
        this.workflow_inputports = workflow_inputports;
    }

    public boolean getIsstart() {
        return isStart;
    }

    public void setIsstart(boolean isStart) {
        this.isStart = isStart;
    }
    public boolean getIsfinish() {
        return isFinish;
    }

    public void setIsfinish(boolean isFinish) {
        this.isFinish = isFinish;
    }

    public workflow_InputPort getWorkflow_inputport() {
        return workflow_inputport;
    }

    public void setWorkflow_inputport(workflow_InputPort workflow_inputport) {
        this.workflow_inputport = workflow_inputport;
    }
    public List<workflow_OutputPort> getWorkflow_outputports() {
        return workflow_outputports;
    }

    public void addWorkflow_outputport(Workflow_outputport workflow_outputport) {
        this.workflow_outputports.add(workflow_outputport);
    }
    public List<workflow_InputPort> getWorkflow_inputports() {
        return workflow_inputports;
    }

    public void addWorkflow_inputport(Workflow_inputport workflow_inputport) {
        this.workflow_inputports.add(workflow_inputport);
    }
    public workflow_Workflow getWorkflow_workflow() {
        return workflow_workflow;
    }

    public void setWorkflow_workflow(workflow_Workflow workflow_workflow) {
        this.workflow_workflow = workflow_workflow;
    }
    public workflow_OutputPort getWorkflow_outputport() {
        return workflow_outputport;
    }

    public void setWorkflow_outputport(workflow_OutputPort workflow_outputport) {
        this.workflow_outputport = workflow_outputport;
    }
    public workflow_Workflow getWorkflow_workflow() {
        return workflow_workflow;
    }

    public void setWorkflow_workflow(workflow_Workflow workflow_workflow) {
        this.workflow_workflow = workflow_workflow;
    }

}