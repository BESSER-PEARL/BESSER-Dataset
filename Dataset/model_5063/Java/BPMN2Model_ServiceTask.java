





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_ServiceTask extends Task {

    private String implementation;





    private BPMN2Model_Operation bpmn2model_operation;


    public BPMN2Model_ServiceTask(
        String implementation    ) {
        super(
        );
        this.implementation = implementation;
    }


    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }

    public BPMN2Model_Operation getBpmn2model_operation() {
        return bpmn2model_operation;
    }

    public void setBpmn2model_operation(BPMN2Model_Operation bpmn2model_operation) {
        this.bpmn2model_operation = bpmn2model_operation;
    }

}