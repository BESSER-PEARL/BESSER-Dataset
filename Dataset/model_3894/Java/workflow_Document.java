





import java.util.List;
import java.util.ArrayList;

public class workflow_Document  {

    private String name;
    private String id;





    private workflow_ActivityI workflow_activityi;




    private workflow_DocumentType workflow_documenttype;




    private workflow_ActivityI workflow_activityi;


    public workflow_Document(
        String name,        String id    ) {
        this.name = name;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public workflow_ActivityI getWorkflow_activityi() {
        return workflow_activityi;
    }

    public void setWorkflow_activityi(workflow_ActivityI workflow_activityi) {
        this.workflow_activityi = workflow_activityi;
    }
    public workflow_DocumentType getWorkflow_documenttype() {
        return workflow_documenttype;
    }

    public void setWorkflow_documenttype(workflow_DocumentType workflow_documenttype) {
        this.workflow_documenttype = workflow_documenttype;
    }
    public workflow_ActivityI getWorkflow_activityi() {
        return workflow_activityi;
    }

    public void setWorkflow_activityi(workflow_ActivityI workflow_activityi) {
        this.workflow_activityi = workflow_activityi;
    }

}