





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_SequenceFlow extends FlowElement {

    private String isImmediate;





    private BPMNProfile_BPMNActivity bpmnprofile_bpmnactivity;


    public BPMNProfile_SequenceFlow(
        String isImmediate    ) {
        super(
        );
        this.isImmediate = isImmediate;
    }


    public String getIsimmediate() {
        return isImmediate;
    }

    public void setIsimmediate(String isImmediate) {
        this.isImmediate = isImmediate;
    }

    public BPMNProfile_BPMNActivity getBpmnprofile_bpmnactivity() {
        return bpmnprofile_bpmnactivity;
    }

    public void setBpmnprofile_bpmnactivity(BPMNProfile_BPMNActivity bpmnprofile_bpmnactivity) {
        this.bpmnprofile_bpmnactivity = bpmnprofile_bpmnactivity;
    }

}