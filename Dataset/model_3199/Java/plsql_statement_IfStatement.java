





import java.util.List;
import java.util.ArrayList;

public class plsql_statement_IfStatement extends Statement {






    private Expression expression;


    public plsql_statement_IfStatement(
    ) {
        super(
        );
    }



    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}