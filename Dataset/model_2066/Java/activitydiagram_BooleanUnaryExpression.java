





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_BooleanUnaryExpression extends BooleanExpression {

    private String operator;





    private activitydiagram_BooleanVariable activitydiagram_booleanvariable;


    public activitydiagram_BooleanUnaryExpression(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public activitydiagram_BooleanVariable getActivitydiagram_booleanvariable() {
        return activitydiagram_booleanvariable;
    }

    public void setActivitydiagram_booleanvariable(activitydiagram_BooleanVariable activitydiagram_booleanvariable) {
        this.activitydiagram_booleanvariable = activitydiagram_booleanvariable;
    }

}