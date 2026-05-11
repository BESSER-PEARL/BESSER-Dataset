





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_BPMNActivity extends FlowNode {

    private String isForCompensation;
    private String completionQuantity;
    private String startQuantity;





    private bpmnprof_SequenceFlow bpmnprof_sequenceflow;


    public bpmnprof_BPMNActivity(
        String isForCompensation,        String completionQuantity,        String startQuantity    ) {
        super(
        );
        this.isForCompensation = isForCompensation;
        this.completionQuantity = completionQuantity;
        this.startQuantity = startQuantity;
    }


    public String getIsforcompensation() {
        return isForCompensation;
    }

    public void setIsforcompensation(String isForCompensation) {
        this.isForCompensation = isForCompensation;
    }
    public String getCompletionquantity() {
        return completionQuantity;
    }

    public void setCompletionquantity(String completionQuantity) {
        this.completionQuantity = completionQuantity;
    }
    public String getStartquantity() {
        return startQuantity;
    }

    public void setStartquantity(String startQuantity) {
        this.startQuantity = startQuantity;
    }

    public bpmnprof_SequenceFlow getBpmnprof_sequenceflow() {
        return bpmnprof_sequenceflow;
    }

    public void setBpmnprof_sequenceflow(bpmnprof_SequenceFlow bpmnprof_sequenceflow) {
        this.bpmnprof_sequenceflow = bpmnprof_sequenceflow;
    }

}