





import java.util.List;
import java.util.ArrayList;

public class workflow_IOutputPort extends IPort {






    private workflow_IWorkflowNode workflow_iworkflownode;




    private List<workflow_ILink> workflow_ilinks;




    private workflow_ILink workflow_ilink;




    private workflow_IWorkflowNode workflow_iworkflownode;


    public workflow_IOutputPort(
    ) {
        super(
        );
        this.workflow_ilinks = new ArrayList<>();
    }

    public workflow_IOutputPort(
        ArrayList<workflow_ILink> workflow_ilinks    ) {
        this.workflow_ilinks = workflow_ilinks;
    }


    public workflow_IWorkflowNode getWorkflow_iworkflownode() {
        return workflow_iworkflownode;
    }

    public void setWorkflow_iworkflownode(workflow_IWorkflowNode workflow_iworkflownode) {
        this.workflow_iworkflownode = workflow_iworkflownode;
    }
    public List<workflow_ILink> getWorkflow_ilinks() {
        return workflow_ilinks;
    }

    public void addWorkflow_ilink(Workflow_ilink workflow_ilink) {
        this.workflow_ilinks.add(workflow_ilink);
    }
    public workflow_ILink getWorkflow_ilink() {
        return workflow_ilink;
    }

    public void setWorkflow_ilink(workflow_ILink workflow_ilink) {
        this.workflow_ilink = workflow_ilink;
    }
    public workflow_IWorkflowNode getWorkflow_iworkflownode() {
        return workflow_iworkflownode;
    }

    public void setWorkflow_iworkflownode(workflow_IWorkflowNode workflow_iworkflownode) {
        this.workflow_iworkflownode = workflow_iworkflownode;
    }

}