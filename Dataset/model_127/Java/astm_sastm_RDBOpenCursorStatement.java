





import java.util.List;
import java.util.ArrayList;

public class astm_sastm_RDBOpenCursorStatement extends RDBCursorStatement {






    private List<Expression> expressions;


    public astm_sastm_RDBOpenCursorStatement(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public astm_sastm_RDBOpenCursorStatement(
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