





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_BooleanVariable extends Variable {






    private activitydiagram_BooleanExpression activitydiagram_booleanexpression;




    private activitydiagram_ControlFlow activitydiagram_controlflow;


    public activitydiagram_BooleanVariable(
    ) {
        super(
        );
    }



    public activitydiagram_BooleanExpression getActivitydiagram_booleanexpression() {
        return activitydiagram_booleanexpression;
    }

    public void setActivitydiagram_booleanexpression(activitydiagram_BooleanExpression activitydiagram_booleanexpression) {
        this.activitydiagram_booleanexpression = activitydiagram_booleanexpression;
    }
    public activitydiagram_ControlFlow getActivitydiagram_controlflow() {
        return activitydiagram_controlflow;
    }

    public void setActivitydiagram_controlflow(activitydiagram_ControlFlow activitydiagram_controlflow) {
        this.activitydiagram_controlflow = activitydiagram_controlflow;
    }

}