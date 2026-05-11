





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_ComplexGateway extends Gateway {






    private BPMN2Model_Expression bpmn2model_expression;




    private BPMN2Model_SequenceFlow bpmn2model_sequenceflow;


    public BPMN2Model_ComplexGateway(
    ) {
        super(
        );
    }



    public BPMN2Model_Expression getBpmn2model_expression() {
        return bpmn2model_expression;
    }

    public void setBpmn2model_expression(BPMN2Model_Expression bpmn2model_expression) {
        this.bpmn2model_expression = bpmn2model_expression;
    }
    public BPMN2Model_SequenceFlow getBpmn2model_sequenceflow() {
        return bpmn2model_sequenceflow;
    }

    public void setBpmn2model_sequenceflow(BPMN2Model_SequenceFlow bpmn2model_sequenceflow) {
        this.bpmn2model_sequenceflow = bpmn2model_sequenceflow;
    }

}