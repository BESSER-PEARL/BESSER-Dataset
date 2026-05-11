





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_IntegerVariable extends Variable, IntegerExpression {

    private int initialValue;





    private activitydiagram_IntegerVariableAssignment activitydiagram_integervariableassignment;


    public activitydiagram_IntegerVariable(
        int initialValue    ) {
        super(
        );
        this.initialValue = initialValue;
    }


    public int getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(int initialValue) {
        this.initialValue = initialValue;
    }

    public activitydiagram_IntegerVariableAssignment getActivitydiagram_integervariableassignment() {
        return activitydiagram_integervariableassignment;
    }

    public void setActivitydiagram_integervariableassignment(activitydiagram_IntegerVariableAssignment activitydiagram_integervariableassignment) {
        this.activitydiagram_integervariableassignment = activitydiagram_integervariableassignment;
    }

}