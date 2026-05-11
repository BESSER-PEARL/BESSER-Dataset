





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_StandardLoopCharacteristics extends LoopCharacteristics {

    private boolean testBefore;



    public BPMN2Model_StandardLoopCharacteristics(
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


}