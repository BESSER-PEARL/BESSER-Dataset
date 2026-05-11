





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_StandardLoopCharacteristics extends LoopCharacteristics {

    private String testBefore;
    private String loopMaximum;





    private BPMNProfile_LoopNode bpmnprofile_loopnode;


    public BPMNProfile_StandardLoopCharacteristics(
        String testBefore,        String loopMaximum    ) {
        super(
        );
        this.testBefore = testBefore;
        this.loopMaximum = loopMaximum;
    }


    public String getTestbefore() {
        return testBefore;
    }

    public void setTestbefore(String testBefore) {
        this.testBefore = testBefore;
    }
    public String getLoopmaximum() {
        return loopMaximum;
    }

    public void setLoopmaximum(String loopMaximum) {
        this.loopMaximum = loopMaximum;
    }

    public BPMNProfile_LoopNode getBpmnprofile_loopnode() {
        return bpmnprofile_loopnode;
    }

    public void setBpmnprofile_loopnode(BPMNProfile_LoopNode bpmnprofile_loopnode) {
        this.bpmnprofile_loopnode = bpmnprofile_loopnode;
    }

}