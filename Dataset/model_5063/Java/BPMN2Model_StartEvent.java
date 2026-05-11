





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_StartEvent extends CatchEvent {

    private boolean isInterrupting;



    public BPMN2Model_StartEvent(
        boolean isInterrupting    ) {
        super(
        );
        this.isInterrupting = isInterrupting;
    }


    public boolean getIsinterrupting() {
        return isInterrupting;
    }

    public void setIsinterrupting(boolean isInterrupting) {
        this.isInterrupting = isInterrupting;
    }


}