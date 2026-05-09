





import java.util.List;
import java.util.ArrayList;

public class DOM_ConstructorInvocation extends Statement {






    private List<Type> types;




    private List<Expression> expressions;


    public DOM_ConstructorInvocation(
    ) {
        super(
        );
        this.types = new ArrayList<>();
        this.expressions = new ArrayList<>();
    }

    public DOM_ConstructorInvocation(
        ArrayList<Type> types,        ArrayList<Expression> expressions    ) {
        this.types = types;
        this.expressions = expressions;
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