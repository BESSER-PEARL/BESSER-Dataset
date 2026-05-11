





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_IntegerCalculationExpression extends IntegerExpression {

    private String operator;



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


}