





import java.util.List;
import java.util.ArrayList;

public class plsql_statement_OpenStatement extends ControlSQLStatement {






    private List<Expression> expressions;


    public plsql_statement_OpenStatement(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public plsql_statement_OpenStatement(
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