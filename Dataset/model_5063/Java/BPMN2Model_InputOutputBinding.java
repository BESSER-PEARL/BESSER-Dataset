





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_InputOutputBinding extends BPMNBase {






    private BPMN2Model_CallableElement bpmn2model_callableelement;




    private BPMN2Model_InputSet bpmn2model_inputset;




    private BPMN2Model_DocumentRoot bpmn2model_documentroot;




    private BPMN2Model_OutputSet bpmn2model_outputset;




    private BPMN2Model_Operation bpmn2model_operation;


    public BPMN2Model_InputOutputBinding(
    ) {
        super(
        );
    }



    public BPMN2Model_CallableElement getBpmn2model_callableelement() {
        return bpmn2model_callableelement;
    }

    public void setBpmn2model_callableelement(BPMN2Model_CallableElement bpmn2model_callableelement) {
        this.bpmn2model_callableelement = bpmn2model_callableelement;
    }
    public BPMN2Model_InputSet getBpmn2model_inputset() {
        return bpmn2model_inputset;
    }

    public void setBpmn2model_inputset(BPMN2Model_InputSet bpmn2model_inputset) {
        this.bpmn2model_inputset = bpmn2model_inputset;
    }
    public BPMN2Model_DocumentRoot getBpmn2model_documentroot() {
        return bpmn2model_documentroot;
    }

    public void setBpmn2model_documentroot(BPMN2Model_DocumentRoot bpmn2model_documentroot) {
        this.bpmn2model_documentroot = bpmn2model_documentroot;
    }
    public BPMN2Model_OutputSet getBpmn2model_outputset() {
        return bpmn2model_outputset;
    }

    public void setBpmn2model_outputset(BPMN2Model_OutputSet bpmn2model_outputset) {
        this.bpmn2model_outputset = bpmn2model_outputset;
    }
    public BPMN2Model_Operation getBpmn2model_operation() {
        return bpmn2model_operation;
    }

    public void setBpmn2model_operation(BPMN2Model_Operation bpmn2model_operation) {
        this.bpmn2model_operation = bpmn2model_operation;
    }

}