





import java.util.List;
import java.util.ArrayList;

public class workflow_ProcessDocument  {

    private String name;





    private workflow_Information workflow_information;


    public workflow_ProcessDocument(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public workflow_Information getWorkflow_information() {
        return workflow_information;
    }

    public void setWorkflow_information(workflow_Information workflow_information) {
        this.workflow_information = workflow_information;
    }

}