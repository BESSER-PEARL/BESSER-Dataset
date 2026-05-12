





import java.util.List;
import java.util.ArrayList;

public class plsql_statement_ForStatement extends LoopStatement {






    private Expression expression;


    public plsql_statement_ForStatement(
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