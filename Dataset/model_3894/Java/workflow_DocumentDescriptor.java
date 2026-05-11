





import java.util.List;
import java.util.ArrayList;

public class workflow_DocumentDescriptor  {

    private String name;





    private workflow_TaskI workflow_taski;




    private workflow_TaskI workflow_taski;




    private workflow_ProcessDocument workflow_processdocument;


    public workflow_DocumentDescriptor(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public workflow_TaskI getWorkflow_taski() {
        return workflow_taski;
    }

    public void setWorkflow_taski(workflow_TaskI workflow_taski) {
        this.workflow_taski = workflow_taski;
    }
    public workflow_TaskI getWorkflow_taski() {
        return workflow_taski;
    }

    public void setWorkflow_taski(workflow_TaskI workflow_taski) {
        this.workflow_taski = workflow_taski;
    }
    public workflow_ProcessDocument getWorkflow_processdocument() {
        return workflow_processdocument;
    }

    public void setWorkflow_processdocument(workflow_ProcessDocument workflow_processdocument) {
        this.workflow_processdocument = workflow_processdocument;
    }

}