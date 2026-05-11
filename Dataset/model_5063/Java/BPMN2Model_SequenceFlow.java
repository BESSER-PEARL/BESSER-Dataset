





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_SequenceFlow extends FlowElement {

    private boolean isImmediate;



    public BPMN2Model_SequenceFlow(
        boolean isImmediate    ) {
        super(
        );
        this.isImmediate = isImmediate;
    }


    public boolean getIsimmediate() {
        return isImmediate;
    }

    public void setIsimmediate(boolean isImmediate) {
        this.isImmediate = isImmediate;
    }


}