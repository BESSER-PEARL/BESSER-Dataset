





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Error extends RootElement {

    private String errorCode;





    private bpmn2_ErrorEventDefinition bpmn2_erroreventdefinition;




    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_Error(
        String errorCode    ) {
        super(
        );
        this.errorCode = errorCode;
    }


    public String getErrorcode() {
        return errorCode;
    }

    public void setErrorcode(String errorCode) {
        this.errorCode = errorCode;
    }

    public bpmn2_ErrorEventDefinition getBpmn2_erroreventdefinition() {
        return bpmn2_erroreventdefinition;
    }

    public void setBpmn2_erroreventdefinition(bpmn2_ErrorEventDefinition bpmn2_erroreventdefinition) {
        this.bpmn2_erroreventdefinition = bpmn2_erroreventdefinition;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}