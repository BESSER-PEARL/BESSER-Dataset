





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_CompensateEventDefinition extends EventDefinition {

    private String waitForCompletion;





    private BPMNProfile_BPMNActivity bpmnprofile_bpmnactivity;


    public BPMNProfile_CompensateEventDefinition(
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

    public BPMNProfile_BPMNActivity getBpmnprofile_bpmnactivity() {
        return bpmnprofile_bpmnactivity;
    }

    public void setBpmnprofile_bpmnactivity(BPMNProfile_BPMNActivity bpmnprofile_bpmnactivity) {
        this.bpmnprofile_bpmnactivity = bpmnprofile_bpmnactivity;
    }

}