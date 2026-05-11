





import java.util.List;
import java.util.ArrayList;

public class plSql_IfStatement extends Statement {






    private plSql_Expression plsql_expression;




    private List<plSql_Statement> plsql_statements;


    public plSql_IfStatement(
    ) {
        super(
        );
        this.plsql_statements = new ArrayList<>();
    }

    public plSql_IfStatement(
        ArrayList<plSql_Statement> plsql_statements    ) {
        this.plsql_statements = plsql_statements;
    }


    public plSql_Expression getPlsql_expression() {
        return plsql_expression;
    }

    public void setPlsql_expression(plSql_Expression plsql_expression) {
        this.plsql_expression = plsql_expression;
    }
    public List<plSql_Statement> getPlsql_statements() {
        return plsql_statements;
    }

    public void addPlsql_statement(Plsql_statement plsql_statement) {
        this.plsql_statements.add(plsql_statement);
    }

}