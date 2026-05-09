





import java.util.List;
import java.util.ArrayList;

public class JavaAbstractSyntax_SuperConstructorInvocation extends Statement {






    private List<Expression> expressions;




    private List<Type> types;




    private Expression expression;


    public JavaAbstractSyntax_SuperConstructorInvocation(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
        this.types = new ArrayList<>();
    }

    public JavaAbstractSyntax_SuperConstructorInvocation(
        ArrayList<Expression> expressions,        ArrayList<Type> types    ) {
        this.expressions = expressions;
        this.types = types;
    }


    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }
    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }
    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}