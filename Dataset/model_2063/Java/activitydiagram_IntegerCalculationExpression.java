





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_IntegerCalculationExpression extends IntegerExpression {

    private String operator;





    private activitydiagram_IntegerVariable activitydiagram_integervariable;


    public activitydiagram_IntegerCalculationExpression(
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

    public activitydiagram_IntegerVariable getActivitydiagram_integervariable() {
        return activitydiagram_integervariable;
    }

    public void setActivitydiagram_integervariable(activitydiagram_IntegerVariable activitydiagram_integervariable) {
        this.activitydiagram_integervariable = activitydiagram_integervariable;
    }

}