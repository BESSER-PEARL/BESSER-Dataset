





import java.util.List;
import java.util.ArrayList;

public class plsql_statement_InsertStatement extends ModifySQLStatement {

    private String columns;
    private String into;





    private List<Expression> expressions;


    public plsql_statement_InsertStatement(
        String columns,        String into    ) {
        super(
        );
        this.columns = columns;
        this.into = into;
        this.expressions = new ArrayList<>();
    }

    public plsql_statement_InsertStatement(
        String columns,        String into        ArrayList<Expression> expressions    ) {
        this.columns = columns;
        this.into = into;
        this.expressions = expressions;
    }

    public String getColumns() {
        return columns;
    }

    public void setColumns(String columns) {
        this.columns = columns;
    }
    public String getInto() {
        return into;
    }

    public void setInto(String into) {
        this.into = into;
    }

    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }

}