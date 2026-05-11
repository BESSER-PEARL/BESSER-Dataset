





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_IntegerBinaryExpression extends IntegerExpression, Expression {

    private boolean operator;



    public activitydiagram_IntegerBinaryExpression(
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


}