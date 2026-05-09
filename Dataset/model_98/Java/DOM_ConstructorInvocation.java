





import java.util.List;
import java.util.ArrayList;

public class DOM_ConstructorInvocation extends Statement {






    private List<Expression> expressions;




    private List<Type> types;


    public DOM_ConstructorInvocation(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
        this.types = new ArrayList<>();
    }

    public DOM_ConstructorInvocation(
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

}