





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_BooleanUnaryExpression extends BooleanExpression {

    private boolean operator;





    private activitydiagram_BooleanExpression activitydiagram_booleanexpression;


    public activitydiagram_BooleanUnaryExpression(
        boolean operator    ) {
        super(
        );
        this.operator = operator;
    }


    public boolean getOperator() {
        return operator;
    }

    public void setOperator(boolean operator) {
        this.operator = operator;
    }

    public activitydiagram_BooleanExpression getActivitydiagram_booleanexpression() {
        return activitydiagram_booleanexpression;
    }

    public void setActivitydiagram_booleanexpression(activitydiagram_BooleanExpression activitydiagram_booleanexpression) {
        this.activitydiagram_booleanexpression = activitydiagram_booleanexpression;
    }

}