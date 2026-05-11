





import java.util.List;
import java.util.ArrayList;

public class workflow_Field  {

    private String name;





    private workflow_DefaultDocumentType workflow_defaultdocumenttype;


    public workflow_Field(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public workflow_DefaultDocumentType getWorkflow_defaultdocumenttype() {
        return workflow_defaultdocumenttype;
    }

    public void setWorkflow_defaultdocumenttype(workflow_DefaultDocumentType workflow_defaultdocumenttype) {
        this.workflow_defaultdocumenttype = workflow_defaultdocumenttype;
    }

}