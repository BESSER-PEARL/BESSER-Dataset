





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_StandardLoopCharacteristics extends LoopCharacteristics {

    private String loopMaximum;
    private String testBefore;





    private bpmnprof_LoopNode bpmnprof_loopnode;




    private bpmnprof_BPMNExpression bpmnprof_bpmnexpression;


    public bpmnprof_StandardLoopCharacteristics(
        String loopMaximum,        String testBefore    ) {
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
    public String getTestbefore() {
        return testBefore;
    }

    public void setTestbefore(String testBefore) {
        this.testBefore = testBefore;
    }

    public bpmnprof_LoopNode getBpmnprof_loopnode() {
        return bpmnprof_loopnode;
    }

    public void setBpmnprof_loopnode(bpmnprof_LoopNode bpmnprof_loopnode) {
        this.bpmnprof_loopnode = bpmnprof_loopnode;
    }
    public bpmnprof_BPMNExpression getBpmnprof_bpmnexpression() {
        return bpmnprof_bpmnexpression;
    }

    public void setBpmnprof_bpmnexpression(bpmnprof_BPMNExpression bpmnprof_bpmnexpression) {
        this.bpmnprof_bpmnexpression = bpmnprof_bpmnexpression;
    }

}