





import java.util.List;
import java.util.ArrayList;

public class workflow_DocumentType  {

    private String name;





    private workflow_DocumentDescriptor workflow_documentdescriptor;




    private workflow_ProcessDocument workflow_processdocument;


    public workflow_DocumentType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public workflow_DocumentDescriptor getWorkflow_documentdescriptor() {
        return workflow_documentdescriptor;
    }

    public void setWorkflow_documentdescriptor(workflow_DocumentDescriptor workflow_documentdescriptor) {
        this.workflow_documentdescriptor = workflow_documentdescriptor;
    }
    public workflow_ProcessDocument getWorkflow_processdocument() {
        return workflow_processdocument;
    }

    public void setWorkflow_processdocument(workflow_ProcessDocument workflow_processdocument) {
        this.workflow_processdocument = workflow_processdocument;
    }

}