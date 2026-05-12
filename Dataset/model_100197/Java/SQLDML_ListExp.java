





import java.util.List;
import java.util.ArrayList;

public class SQLDML_ListExp extends Predicate {






    private List<Expression> expressions;


    public SQLDML_ListExp(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public SQLDML_ListExp(
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