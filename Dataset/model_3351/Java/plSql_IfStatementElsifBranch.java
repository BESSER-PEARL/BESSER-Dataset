





import java.util.List;
import java.util.ArrayList;

public class plSql_IfStatementElsifBranch  {






    private plSql_Expression plsql_expression;




    private plSql_IfStatement plsql_ifstatement;




    private List<plSql_Statement> plsql_statements;


    public plSql_IfStatementElsifBranch(
    ) {
        this.plsql_statements = new ArrayList<>();
    }

    public plSql_IfStatementElsifBranch(
        ArrayList<plSql_Statement> plsql_statements    ) {
        this.plsql_statements = plsql_statements;
    }


    public plSql_Expression getPlsql_expression() {
        return plsql_expression;
    }

    public void setPlsql_expression(plSql_Expression plsql_expression) {
        this.plsql_expression = plsql_expression;
    }
    public plSql_IfStatement getPlsql_ifstatement() {
        return plsql_ifstatement;
    }

    public void setPlsql_ifstatement(plSql_IfStatement plsql_ifstatement) {
        this.plsql_ifstatement = plsql_ifstatement;
    }
    public List<plSql_Statement> getPlsql_statements() {
        return plsql_statements;
    }

    public void addPlsql_statement(Plsql_statement plsql_statement) {
        this.plsql_statements.add(plsql_statement);
    }

}