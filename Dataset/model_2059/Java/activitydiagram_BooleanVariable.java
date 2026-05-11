





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_BooleanVariable extends BooleanExpression, Variable {

    private boolean currentValue;
    private boolean initialValue;





    private activitydiagram_ControlFlow activitydiagram_controlflow;


    public activitydiagram_BooleanVariable(
        boolean currentValue,        boolean initialValue    ) {
        super(
        );
        this.currentValue = currentValue;
        this.initialValue = initialValue;
    }


    public boolean getCurrentvalue() {
        return currentValue;
    }

    public void setCurrentvalue(boolean currentValue) {
        this.currentValue = currentValue;
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