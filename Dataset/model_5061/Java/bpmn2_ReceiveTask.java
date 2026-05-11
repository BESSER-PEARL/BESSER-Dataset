





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ReceiveTask extends Task {

    private boolean instantiate;
    private String implementation;





    private bpmn2_Operation bpmn2_operation;




    private bpmn2_Message bpmn2_message;


    public bpmn2_ReceiveTask(
        boolean instantiate,        String implementation    ) {
        super(
        );
        this.instantiate = instantiate;
        this.implementation = implementation;
    }


    public boolean getInstantiate() {
        return instantiate;
    }

    public void setInstantiate(boolean instantiate) {
        this.instantiate = instantiate;
    }
    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }

    public bpmn2_Operation getBpmn2_operation() {
        return bpmn2_operation;
    }

    public void setBpmn2_operation(bpmn2_Operation bpmn2_operation) {
        this.bpmn2_operation = bpmn2_operation;
    }
    public bpmn2_Message getBpmn2_message() {
        return bpmn2_message;
    }

    public void setBpmn2_message(bpmn2_Message bpmn2_message) {
        this.bpmn2_message = bpmn2_message;
    }

}