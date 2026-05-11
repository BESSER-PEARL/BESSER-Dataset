





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_ComplexGateway extends NonExclusiveGateway {






    private BPMNProfile_BPMNExpression bpmnprofile_bpmnexpression;




    private BPMNProfile_SequenceFlow bpmnprofile_sequenceflow;


    public BPMNProfile_ComplexGateway(
    ) {
        super(
        );
    }



    public BPMNProfile_BPMNExpression getBpmnprofile_bpmnexpression() {
        return bpmnprofile_bpmnexpression;
    }

    public void setBpmnprofile_bpmnexpression(BPMNProfile_BPMNExpression bpmnprofile_bpmnexpression) {
        this.bpmnprofile_bpmnexpression = bpmnprofile_bpmnexpression;
    }
    public BPMNProfile_SequenceFlow getBpmnprofile_sequenceflow() {
        return bpmnprofile_sequenceflow;
    }

    public void setBpmnprofile_sequenceflow(BPMNProfile_SequenceFlow bpmnprofile_sequenceflow) {
        this.bpmnprofile_sequenceflow = bpmnprofile_sequenceflow;
    }

}