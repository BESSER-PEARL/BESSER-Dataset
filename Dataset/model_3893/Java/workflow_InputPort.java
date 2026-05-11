





import java.util.List;
import java.util.ArrayList;

public class workflow_InputPort extends Port {






    private workflow_WorkflowNode workflow_workflownode;




    private workflow_WorkflowNode workflow_workflownode;




    private workflow_Edge workflow_edge;




    private List<workflow_Edge> workflow_edges;


    public workflow_InputPort(
    ) {
        super(
        );
        this.workflow_edges = new ArrayList<>();
    }

    public workflow_InputPort(
        ArrayList<workflow_Edge> workflow_edges    ) {
        this.workflow_edges = workflow_edges;
    }


    public workflow_WorkflowNode getWorkflow_workflownode() {
        return workflow_workflownode;
    }

    public void setWorkflow_workflownode(workflow_WorkflowNode workflow_workflownode) {
        this.workflow_workflownode = workflow_workflownode;
    }
    public workflow_WorkflowNode getWorkflow_workflownode() {
        return workflow_workflownode;
    }

    public void setWorkflow_workflownode(workflow_WorkflowNode workflow_workflownode) {
        this.workflow_workflownode = workflow_workflownode;
    }
    public workflow_Edge getWorkflow_edge() {
        return workflow_edge;
    }

    public void setWorkflow_edge(workflow_Edge workflow_edge) {
        this.workflow_edge = workflow_edge;
    }
    public List<workflow_Edge> getWorkflow_edges() {
        return workflow_edges;
    }

    public void addWorkflow_edge(Workflow_edge workflow_edge) {
        this.workflow_edges.add(workflow_edge);
    }

}