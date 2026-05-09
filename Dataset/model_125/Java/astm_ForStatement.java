





import java.util.List;
import java.util.ArrayList;

public class astm_ForStatement extends LoopStatement {






    private List<Expression> expressions;




    private Expression expression;


    public astm_ForStatement(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public astm_ForStatement(
        ArrayList<Expression> expressions    ) {
        this.expressions = expressions;
    }


    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }
    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}