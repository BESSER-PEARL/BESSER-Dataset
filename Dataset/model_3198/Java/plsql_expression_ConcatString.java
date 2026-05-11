





import java.util.List;
import java.util.ArrayList;

public class plsql_expression_ConcatString extends StringOperation {






    private List<Expression> expressions;


    public plsql_expression_ConcatString(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public plsql_expression_ConcatString(
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