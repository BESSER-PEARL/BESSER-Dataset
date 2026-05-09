





import java.util.List;
import java.util.ArrayList;

public class statements_StatementListContainer extends Commentable {






    private List<Statement> statements;


    public statements_StatementListContainer(
    ) {
        super(
        );
        this.statements = new ArrayList<>();
    }

    public statements_StatementListContainer(
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