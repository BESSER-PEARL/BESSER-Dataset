





import java.util.List;
import java.util.ArrayList;

public class ACG_CollectionExp extends LiteralExp {






    private List<Expression> expressions;


    public ACG_CollectionExp(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public ACG_CollectionExp(
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