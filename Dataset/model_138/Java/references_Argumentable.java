





import java.util.List;
import java.util.ArrayList;

public class references_Argumentable extends Commentable {






    private List<Expression> expressions;


    public references_Argumentable(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public references_Argumentable(
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