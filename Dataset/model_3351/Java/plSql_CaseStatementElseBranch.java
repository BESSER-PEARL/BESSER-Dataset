





import java.util.List;
import java.util.ArrayList;

public class plSql_CaseStatementElseBranch  {






    private List<plSql_Statement> plsql_statements;




    private plSql_CaseStatement plsql_casestatement;


    public plSql_CaseStatementElseBranch(
    ) {
        this.plsql_statements = new ArrayList<>();
    }

    public plSql_CaseStatementElseBranch(
        ArrayList<plSql_Statement> plsql_statements    ) {
        this.plsql_statements = plsql_statements;
    }


    public List<plSql_Statement> getPlsql_statements() {
        return plsql_statements;
    }

    public void addPlsql_statement(Plsql_statement plsql_statement) {
        this.plsql_statements.add(plsql_statement);
    }
    public plSql_CaseStatement getPlsql_casestatement() {
        return plsql_casestatement;
    }

    public void setPlsql_casestatement(plSql_CaseStatement plsql_casestatement) {
        this.plsql_casestatement = plsql_casestatement;
    }

}