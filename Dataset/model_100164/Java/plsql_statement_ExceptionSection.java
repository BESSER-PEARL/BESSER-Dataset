





import java.util.List;
import java.util.ArrayList;

public class plsql_statement_ExceptionSection  {

    private String exceptionNames;





    private List<Statement> statements;


    public plsql_statement_ExceptionSection(
        String exceptionNames    ) {
        this.exceptionNames = exceptionNames;
        this.statements = new ArrayList<>();
    }

    public plsql_statement_ExceptionSection(
        String exceptionNames        ArrayList<Statement> statements    ) {
        this.exceptionNames = exceptionNames;
        this.statements = statements;
    }

    public String getExceptionnames() {
        return exceptionNames;
    }

    public void setExceptionnames(String exceptionNames) {
        this.exceptionNames = exceptionNames;
    }

    public List<Statement> getStatements() {
        return statements;
    }

    public void addStatement(Statement statement) {
        this.statements.add(statement);
    }

}