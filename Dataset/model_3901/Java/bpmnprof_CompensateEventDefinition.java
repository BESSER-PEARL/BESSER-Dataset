





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_CompensateEventDefinition extends EventDefinition {

    private String waitForCompletion;





    private bpmnprof_BPMNActivity bpmnprof_bpmnactivity;


    public bpmnprof_CompensateEventDefinition(
        String waitForCompletion    ) {
        super(
        );
        this.waitForCompletion = waitForCompletion;
    }


    public String getWaitforcompletion() {
        return waitForCompletion;
    }

    public void setWaitforcompletion(String waitForCompletion) {
        this.waitForCompletion = waitForCompletion;
    }

    public bpmnprof_BPMNActivity getBpmnprof_bpmnactivity() {
        return bpmnprof_bpmnactivity;
    }

    public void setBpmnprof_bpmnactivity(bpmnprof_BPMNActivity bpmnprof_bpmnactivity) {
        this.bpmnprof_bpmnactivity = bpmnprof_bpmnactivity;
    }

}