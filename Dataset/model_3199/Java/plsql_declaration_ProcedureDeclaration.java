





import java.util.List;
import java.util.ArrayList;

public class plsql_declaration_ProcedureDeclaration extends Declaration {






    private List<Statement> statements;


    public plsql_declaration_ProcedureDeclaration(
    ) {
        super(
        );
        this.statements = new ArrayList<>();
    }

    public plsql_declaration_ProcedureDeclaration(
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