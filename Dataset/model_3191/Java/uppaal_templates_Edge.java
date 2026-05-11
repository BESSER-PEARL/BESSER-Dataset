





import java.util.List;
import java.util.ArrayList;

public class uppaal_templates_Edge extends core_CommentableElement, visuals_LinearElement, visuals_ColoredElement {






    private Expression expression;




    private List<Expression> expressions;


    public uppaal_templates_Edge(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public uppaal_templates_Edge(
        ArrayList<Expression> expressions    ) {
        this.expressions = expressions;
    }


    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }
    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }

}