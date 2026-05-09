





import java.util.List;
import java.util.ArrayList;

public class gastm_CaseBlock extends SwitchCase {






    private List<Expression> expressions;


    public gastm_CaseBlock(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public gastm_CaseBlock(
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