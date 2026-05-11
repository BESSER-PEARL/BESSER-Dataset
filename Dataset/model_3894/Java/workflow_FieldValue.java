





import java.util.List;
import java.util.ArrayList;

public class workflow_FieldValue  {

    private String value;





    private workflow_Field workflow_field;




    private workflow_DefaultDocument workflow_defaultdocument;


    public workflow_FieldValue(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public workflow_Field getWorkflow_field() {
        return workflow_field;
    }

    public void setWorkflow_field(workflow_Field workflow_field) {
        this.workflow_field = workflow_field;
    }
    public workflow_DefaultDocument getWorkflow_defaultdocument() {
        return workflow_defaultdocument;
    }

    public void setWorkflow_defaultdocument(workflow_DefaultDocument workflow_defaultdocument) {
        this.workflow_defaultdocument = workflow_defaultdocument;
    }

}