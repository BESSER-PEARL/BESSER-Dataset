





import java.util.List;
import java.util.ArrayList;

public class bpmn2_StandardLoopCharacteristics extends LoopCharacteristics {

    private boolean testBefore;





    private bpmn2_Expression bpmn2_expression;




    private bpmn2_Expression bpmn2_expression;


    public bpmn2_StandardLoopCharacteristics(
        boolean testBefore    ) {
        super(
        );
        this.testBefore = testBefore;
    }


    public boolean getTestbefore() {
        return testBefore;
    }

    public void setTestbefore(boolean testBefore) {
        this.testBefore = testBefore;
    }

    public bpmn2_Expression getBpmn2_expression() {
        return bpmn2_expression;
    }

    public void setBpmn2_expression(bpmn2_Expression bpmn2_expression) {
        this.bpmn2_expression = bpmn2_expression;
    }
    public bpmn2_Expression getBpmn2_expression() {
        return bpmn2_expression;
    }

    public void setBpmn2_expression(bpmn2_Expression bpmn2_expression) {
        this.bpmn2_expression = bpmn2_expression;
    }

}