





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_IntegerComparisonExpression extends BooleanExpression {

    private String operator;



    public activitydiagram_IntegerComparisonExpression(
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