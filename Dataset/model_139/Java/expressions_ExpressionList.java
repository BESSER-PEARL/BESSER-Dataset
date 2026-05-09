





import java.util.List;
import java.util.ArrayList;

public class expressions_ExpressionList extends ForLoopInitializer {






    private List<Expression> expressions;


    public expressions_ExpressionList(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public expressions_ExpressionList(
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