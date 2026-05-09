





import java.util.List;
import java.util.ArrayList;

public class astm_sastm_RDBInsertStatement extends Statement {






    private List<Expression> expressions;


    public astm_sastm_RDBInsertStatement(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public astm_sastm_RDBInsertStatement(
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