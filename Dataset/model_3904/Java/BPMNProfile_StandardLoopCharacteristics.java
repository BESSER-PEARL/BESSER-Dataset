





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_StandardLoopCharacteristics extends LoopCharacteristics {

    private String loopMaximum;
    private String testBefore;





    private BPMNProfile_BPMNExpression bpmnprofile_bpmnexpression;


    public BPMNProfile_StandardLoopCharacteristics(
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

    public BPMNProfile_BPMNExpression getBpmnprofile_bpmnexpression() {
        return bpmnprofile_bpmnexpression;
    }

    public void setBpmnprofile_bpmnexpression(BPMNProfile_BPMNExpression bpmnprofile_bpmnexpression) {
        this.bpmnprofile_bpmnexpression = bpmnprofile_bpmnexpression;
    }

}