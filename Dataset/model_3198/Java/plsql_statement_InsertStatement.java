





import java.util.List;
import java.util.ArrayList;

public class plsql_statement_InsertStatement extends ModifySQLStatement {

    private String into;
    private String columns;





    private List<Expression> expressions;


    public plsql_statement_InsertStatement(
        String into,        String columns    ) {
        super(
        );
        this.into = into;
        this.columns = columns;
        this.expressions = new ArrayList<>();
    }

    public plsql_statement_InsertStatement(
        String into,        String columns        ArrayList<Expression> expressions    ) {
        this.into = into;
        this.columns = columns;
        this.expressions = expressions;
    }

    public String getInto() {
        return into;
    }

    public void setInto(String into) {
        this.into = into;
    }
    public String getColumns() {
        return columns;
    }

    public void setColumns(String columns) {
        this.columns = columns;
    }

    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }

}