





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Error extends RootElement {

    private String errorCode;
    private String name;





    private bpmn2_ErrorEventDefinition bpmn2_erroreventdefinition;


    public bpmn2_Error(
        String errorCode,        String name    ) {
        super(
        );
        this.errorCode = errorCode;
        this.name = name;
    }


    public String getErrorcode() {
        return errorCode;
    }

    public void setErrorcode(String errorCode) {
        this.errorCode = errorCode;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_ErrorEventDefinition getBpmn2_erroreventdefinition() {
        return bpmn2_erroreventdefinition;
    }

    public void setBpmn2_erroreventdefinition(bpmn2_ErrorEventDefinition bpmn2_erroreventdefinition) {
        this.bpmn2_erroreventdefinition = bpmn2_erroreventdefinition;
    }

}