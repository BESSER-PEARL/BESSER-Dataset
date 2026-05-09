





import java.util.List;
import java.util.ArrayList;

public class simTL4J_expressions_ExpressionList extends ForLoopInitializer {






    private List<Expression> expressions;


    public simTL4J_expressions_ExpressionList(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public simTL4J_expressions_ExpressionList(
        ArrayList<Expression> expressions    ) {
        this.expressions = expressions;
    }


    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }

}