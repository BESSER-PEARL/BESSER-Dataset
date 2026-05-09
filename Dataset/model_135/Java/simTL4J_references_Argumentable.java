





import java.util.List;
import java.util.ArrayList;

public class simTL4J_references_Argumentable extends Commentable {






    private List<Expression> expressions;


    public simTL4J_references_Argumentable(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public simTL4J_references_Argumentable(
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