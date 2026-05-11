





import java.util.List;
import java.util.ArrayList;

public class plSql_StatementBody  {

    private String endName;





    private List<plSql_Statement> plsql_statements;




    private plSql_ProcedureImplementation plsql_procedureimplementation;


    public plSql_StatementBody(
        String endName    ) {
        this.endName = endName;
        this.plsql_statements = new ArrayList<>();
    }

    public plSql_StatementBody(
        String endName        ArrayList<plSql_Statement> plsql_statements    ) {
        this.endName = endName;
        this.plsql_statements = plsql_statements;
    }

    public String getEndname() {
        return endName;
    }

    public void setEndname(String endName) {
        this.endName = endName;
    }

    public List<plSql_Statement> getPlsql_statements() {
        return plsql_statements;
    }

    public void addPlsql_statement(Plsql_statement plsql_statement) {
        this.plsql_statements.add(plsql_statement);
    }
    public plSql_ProcedureImplementation getPlsql_procedureimplementation() {
        return plsql_procedureimplementation;
    }

    public void setPlsql_procedureimplementation(plSql_ProcedureImplementation plsql_procedureimplementation) {
        this.plsql_procedureimplementation = plsql_procedureimplementation;
    }

}