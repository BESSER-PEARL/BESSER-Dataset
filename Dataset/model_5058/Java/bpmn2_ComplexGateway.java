





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ComplexGateway extends Gateway {






    private bpmn2_SequenceFlow bpmn2_sequenceflow;




    private bpmn2_Expression bpmn2_expression;


    public bpmn2_ComplexGateway(
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
    public bpmn2_Expression getBpmn2_expression() {
        return bpmn2_expression;
    }

    public void setBpmn2_expression(bpmn2_Expression bpmn2_expression) {
        this.bpmn2_expression = bpmn2_expression;
    }

}