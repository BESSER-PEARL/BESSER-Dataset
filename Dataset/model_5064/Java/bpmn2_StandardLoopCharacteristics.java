





import java.util.List;
import java.util.ArrayList;

public class bpmn2_StandardLoopCharacteristics extends LoopCharacteristics {

    private String loopMaximum;
    private boolean testBefore;





    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_Expression bpmn2_expression;


    public bpmn2_StandardLoopCharacteristics(
        String loopMaximum,        boolean testBefore    ) {
        super(
        );
        this.loopMaximum = loopMaximum;
        this.testBefore = testBefore;
    }


    public String getLoopmaximum() {
        return loopMaximum;
    }

    public void setLoopmaximum(String loopMaximum) {
        this.loopMaximum = loopMaximum;
    }
    public boolean getTestbefore() {
        return testBefore;
    }

    public void setTestbefore(boolean testBefore) {
        this.testBefore = testBefore;
    }

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_Expression getBpmn2_expression() {
        return bpmn2_expression;
    }

    public void setBpmn2_expression(bpmn2_Expression bpmn2_expression) {
        this.bpmn2_expression = bpmn2_expression;
    }

}