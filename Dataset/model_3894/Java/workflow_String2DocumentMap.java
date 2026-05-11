





import java.util.List;
import java.util.ArrayList;

public class workflow_String2DocumentMap  {

    private String key;





    private workflow_Document workflow_document;




    private workflow_CaseI workflow_casei;


    public workflow_String2DocumentMap(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public workflow_Document getWorkflow_document() {
        return workflow_document;
    }

    public void setWorkflow_document(workflow_Document workflow_document) {
        this.workflow_document = workflow_document;
    }
    public workflow_CaseI getWorkflow_casei() {
        return workflow_casei;
    }

    public void setWorkflow_casei(workflow_CaseI workflow_casei) {
        this.workflow_casei = workflow_casei;
    }

}