





import java.util.List;
import java.util.ArrayList;

public class frontend_core_ClosureDeclaration extends Expression {






    private List<Statement> statements;


    public frontend_core_ClosureDeclaration(
    ) {
        super(
        );
        this.statements = new ArrayList<>();
    }

    public frontend_core_ClosureDeclaration(
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