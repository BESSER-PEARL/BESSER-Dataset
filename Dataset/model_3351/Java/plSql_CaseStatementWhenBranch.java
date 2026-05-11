





import java.util.List;
import java.util.ArrayList;

public class plSql_CaseStatementWhenBranch  {






    private plSql_CaseStatement plsql_casestatement;




    private plSql_Expression plsql_expression;




    private List<plSql_Statement> plsql_statements;


    public plSql_CaseStatementWhenBranch(
    ) {
        this.plsql_statements = new ArrayList<>();
    }

    public plSql_CaseStatementWhenBranch(
        ArrayList<plSql_Statement> plsql_statements    ) {
        this.plsql_statements = plsql_statements;
    }


    public plSql_CaseStatement getPlsql_casestatement() {
        return plsql_casestatement;
    }

    public void setPlsql_casestatement(plSql_CaseStatement plsql_casestatement) {
        this.plsql_casestatement = plsql_casestatement;
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