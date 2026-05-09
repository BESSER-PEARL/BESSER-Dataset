





import java.util.List;
import java.util.ArrayList;

public class simTL4J_statements_ForLoop extends statements_StatementContainer, statements_Statement, statements_Conditional {






    private List<Expression> expressions;


    public simTL4J_statements_ForLoop(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public simTL4J_statements_ForLoop(
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