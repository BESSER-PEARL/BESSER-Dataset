





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_IntegerBinaryExpression extends IntegerExpression, Expression {

    private String operator;



    public activitydiagram_IntegerBinaryExpression(
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