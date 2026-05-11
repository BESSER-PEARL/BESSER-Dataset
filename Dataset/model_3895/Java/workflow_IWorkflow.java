





import java.util.List;
import java.util.ArrayList;

public class workflow_IWorkflow extends IWorkflowElement {






    private List<workflow_IWorkflowNode> workflow_iworkflownodes;




    private workflow_IWorkflowNode workflow_iworkflownode;




    private workflow_ILink workflow_ilink;




    private List<workflow_ILink> workflow_ilinks;


    public workflow_IWorkflow(
    ) {
        super(
        );
        this.workflow_iworkflownodes = new ArrayList<>();
        this.workflow_ilinks = new ArrayList<>();
    }

    public workflow_IWorkflow(
        ArrayList<workflow_IWorkflowNode> workflow_iworkflownodes,        ArrayList<workflow_ILink> workflow_ilinks    ) {
        this.workflow_iworkflownodes = workflow_iworkflownodes;
        this.workflow_ilinks = workflow_ilinks;
    }


    public List<workflow_IWorkflowNode> getWorkflow_iworkflownodes() {
        return workflow_iworkflownodes;
    }

    public void addWorkflow_iworkflownode(Workflow_iworkflownode workflow_iworkflownode) {
        this.workflow_iworkflownodes.add(workflow_iworkflownode);
    }
    public workflow_IWorkflowNode getWorkflow_iworkflownode() {
        return workflow_iworkflownode;
    }

    public void setWorkflow_iworkflownode(workflow_IWorkflowNode workflow_iworkflownode) {
        this.workflow_iworkflownode = workflow_iworkflownode;
    }
    public workflow_ILink getWorkflow_ilink() {
        return workflow_ilink;
    }

    public void setWorkflow_ilink(workflow_ILink workflow_ilink) {
        this.workflow_ilink = workflow_ilink;
    }
    public List<workflow_ILink> getWorkflow_ilinks() {
        return workflow_ilinks;
    }

    public void addWorkflow_ilink(Workflow_ilink workflow_ilink) {
        this.workflow_ilinks.add(workflow_ilink);
    }

}