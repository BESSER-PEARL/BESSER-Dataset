





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_ReceiveTask extends Task {

    private String implementation;
    private boolean instantiate;





    private BPMN2Model_Operation bpmn2model_operation;




    private BPMN2Model_Message bpmn2model_message;


    public BPMN2Model_ReceiveTask(
        String implementation,        boolean instantiate    ) {
        super(
        );
        this.implementation = implementation;
        this.instantiate = instantiate;
    }


    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }
    public boolean getInstantiate() {
        return instantiate;
    }

    public void setInstantiate(boolean instantiate) {
        this.instantiate = instantiate;
    }

    public BPMN2Model_Operation getBpmn2model_operation() {
        return bpmn2model_operation;
    }

    public void setBpmn2model_operation(BPMN2Model_Operation bpmn2model_operation) {
        this.bpmn2model_operation = bpmn2model_operation;
    }
    public BPMN2Model_Message getBpmn2model_message() {
        return bpmn2model_message;
    }

    public void setBpmn2model_message(BPMN2Model_Message bpmn2model_message) {
        this.bpmn2model_message = bpmn2model_message;
    }

}