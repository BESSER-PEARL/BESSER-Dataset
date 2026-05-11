





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_BooleanVariable extends Variable, BooleanExpression {

    private boolean initialValue;





    private activitydiagram_ControlFlow activitydiagram_controlflow;


    public activitydiagram_BooleanVariable(
        boolean initialValue    ) {
        super(
        );
        this.initialValue = initialValue;
    }


    public boolean getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(boolean initialValue) {
        this.initialValue = initialValue;
    }

    public activitydiagram_ControlFlow getActivitydiagram_controlflow() {
        return activitydiagram_controlflow;
    }

    public void setActivitydiagram_controlflow(activitydiagram_ControlFlow activitydiagram_controlflow) {
        this.activitydiagram_controlflow = activitydiagram_controlflow;
    }

}