





import java.util.List;
import java.util.ArrayList;

public class simTL4J_arrays_ArrayInstantiationBySize extends arrays_ArrayTypeable, types_TypedElement, references_Reference, expressions_Expression {






    private List<Expression> expressions;


    public simTL4J_arrays_ArrayInstantiationBySize(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public simTL4J_arrays_ArrayInstantiationBySize(
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