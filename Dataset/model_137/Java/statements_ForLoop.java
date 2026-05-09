





import java.util.List;
import java.util.ArrayList;

public class statements_ForLoop extends StatementContainer, Conditional, Statement {






    private List<Expression> expressions;


    public statements_ForLoop(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public statements_ForLoop(
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