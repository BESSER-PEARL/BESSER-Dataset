





import java.util.List;
import java.util.ArrayList;

public class DVE_model_ArrayLiteral extends Literal {






    private List<Expression> expressions;


    public DVE_model_ArrayLiteral(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public DVE_model_ArrayLiteral(
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