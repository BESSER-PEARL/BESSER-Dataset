





import java.util.List;
import java.util.ArrayList;

public class bpmn2_InputOutputBinding  {

    private String id;





    private bpmn2_InputSet bpmn2_inputset;




    private bpmn2_Operation bpmn2_operation;




    private bpmn2_OutputSet bpmn2_outputset;




    private bpmn2_CallableElement bpmn2_callableelement;


    public bpmn2_InputOutputBinding(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public bpmn2_InputSet getBpmn2_inputset() {
        return bpmn2_inputset;
    }

    public void setBpmn2_inputset(bpmn2_InputSet bpmn2_inputset) {
        this.bpmn2_inputset = bpmn2_inputset;
    }
    public bpmn2_Operation getBpmn2_operation() {
        return bpmn2_operation;
    }

    public void setBpmn2_operation(bpmn2_Operation bpmn2_operation) {
        this.bpmn2_operation = bpmn2_operation;
    }
    public bpmn2_OutputSet getBpmn2_outputset() {
        return bpmn2_outputset;
    }

    public void setBpmn2_outputset(bpmn2_OutputSet bpmn2_outputset) {
        this.bpmn2_outputset = bpmn2_outputset;
    }
    public bpmn2_CallableElement getBpmn2_callableelement() {
        return bpmn2_callableelement;
    }

    public void setBpmn2_callableelement(bpmn2_CallableElement bpmn2_callableelement) {
        this.bpmn2_callableelement = bpmn2_callableelement;
    }

}