





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_ExclusiveGateway extends Gateway {






    private BPMN2Model_SequenceFlow bpmn2model_sequenceflow;


    public BPMN2Model_ExclusiveGateway(
    ) {
        super(
        );
    }



    public BPMN2Model_SequenceFlow getBpmn2model_sequenceflow() {
        return bpmn2model_sequenceflow;
    }

    public void setBpmn2model_sequenceflow(BPMN2Model_SequenceFlow bpmn2model_sequenceflow) {
        this.bpmn2model_sequenceflow = bpmn2model_sequenceflow;
    }

}