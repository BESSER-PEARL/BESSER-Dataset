





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ExclusiveGateway extends Gateway {






    private bpmn2_SequenceFlow bpmn2_sequenceflow;


    public bpmn2_ExclusiveGateway(
    ) {
        super(
        );
    }



    public bpmn2_SequenceFlow getBpmn2_sequenceflow() {
        return bpmn2_sequenceflow;
    }

    public void setBpmn2_sequenceflow(bpmn2_SequenceFlow bpmn2_sequenceflow) {
        this.bpmn2_sequenceflow = bpmn2_sequenceflow;
    }

}