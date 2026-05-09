





import java.util.List;
import java.util.ArrayList;

public class statements_Assert extends Statement, Conditional {






    private Expression expression;


    public statements_Assert(
    ) {
        super(
        );
    }



    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}