





import java.util.List;
import java.util.ArrayList;

public class DOM_SuperConstructorInvocation extends Statement {






    private Expression expression;




    private List<Type> types;




    private List<Expression> expressions;


    public DOM_SuperConstructorInvocation(
    ) {
        super(
        );
        this.types = new ArrayList<>();
        this.expressions = new ArrayList<>();
    }

    public DOM_SuperConstructorInvocation(
        ArrayList<Type> types,        ArrayList<Expression> expressions    ) {
        this.types = types;
        this.expressions = expressions;
    }


    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }
    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }
    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }

}