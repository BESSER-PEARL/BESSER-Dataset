





import java.util.List;
import java.util.ArrayList;

public class JavaAbstractSyntax_ForStatement extends Statement {






    private List<Expression> expressions;




    private Expression expression;




    private List<Expression> expressions;


    public JavaAbstractSyntax_ForStatement(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
        this.expressions = new ArrayList<>();
    }

    public JavaAbstractSyntax_ForStatement(
        ArrayList<Expression> expressions,        ArrayList<Expression> expressions    ) {
        this.expressions = expressions;
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
    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }

}