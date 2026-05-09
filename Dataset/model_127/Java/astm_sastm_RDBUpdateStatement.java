





import java.util.List;
import java.util.ArrayList;

public class astm_sastm_RDBUpdateStatement extends RDBModifyStatement {






    private List<Expression> expressions;


    public astm_sastm_RDBUpdateStatement(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public astm_sastm_RDBUpdateStatement(
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