





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_BooleanUnaryExpression extends BooleanExpression {

    private boolean operator;



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


}