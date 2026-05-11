





import java.util.List;
import java.util.ArrayList;

public class plsql_statement_UpdatePair  {

    private String column;





    private Expression expression;


    public plsql_statement_UpdatePair(
        String column    ) {
        this.column = column;
    }


    public String getColumn() {
        return column;
    }

    public void setColumn(String column) {
        this.column = column;
    }

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}