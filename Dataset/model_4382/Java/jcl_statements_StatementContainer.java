





import java.util.List;
import java.util.ArrayList;

public class jcl_statements_StatementContainer  {






    private List<Statement> statements;


    public jcl_statements_StatementContainer(
    ) {
        this.statements = new ArrayList<>();
    }

    public jcl_statements_StatementContainer(
        ArrayList<Statement> statements    ) {
        this.statements = statements;
    }


    public List<Statement> getStatements() {
        return statements;
    }

    public void addStatement(Statement statement) {
        this.statements.add(statement);
    }

}