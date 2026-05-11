





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ServiceTask extends Task {

    private String implementation;





    private bpmn2_Operation bpmn2_operation;


    public bpmn2_ServiceTask(
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

    public bpmn2_Operation getBpmn2_operation() {
        return bpmn2_operation;
    }

    public void setBpmn2_operation(bpmn2_Operation bpmn2_operation) {
        this.bpmn2_operation = bpmn2_operation;
    }

}