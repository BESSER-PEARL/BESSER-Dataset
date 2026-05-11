





import java.util.List;
import java.util.ArrayList;

public class workflow_AbstractTask extends NamedElement {

    private String status;





    private List<workflow_TaskOutput> workflow_taskoutputs;


    public workflow_AbstractTask(
        String status    ) {
        super(
        );
        this.status = status;
        this.workflow_taskoutputs = new ArrayList<>();
    }

    public workflow_AbstractTask(
        String status        ArrayList<workflow_TaskOutput> workflow_taskoutputs    ) {
        this.status = status;
        this.workflow_taskoutputs = workflow_taskoutputs;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public List<workflow_TaskOutput> getWorkflow_taskoutputs() {
        return workflow_taskoutputs;
    }

    public void addWorkflow_taskoutput(Workflow_taskoutput workflow_taskoutput) {
        this.workflow_taskoutputs.add(workflow_taskoutput);
    }

}