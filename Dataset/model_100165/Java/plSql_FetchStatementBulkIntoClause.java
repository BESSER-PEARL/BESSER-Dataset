





import java.util.List;
import java.util.ArrayList;

public class plSql_FetchStatementBulkIntoClause extends FetchStatementIntoClause {






    private plSql_Expression plsql_expression;


    public plSql_FetchStatementBulkIntoClause(
    ) {
        super(
        );
    }



    public plSql_Expression getPlsql_expression() {
        return plsql_expression;
    }

    public void setPlsql_expression(plSql_Expression plsql_expression) {
        this.plsql_expression = plsql_expression;
    }

}