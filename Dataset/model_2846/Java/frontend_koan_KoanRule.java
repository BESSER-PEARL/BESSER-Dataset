





import java.util.List;
import java.util.ArrayList;

public class frontend_koan_KoanRule extends core_NamedElement, core_LocatedElement {






    private List<Statement> statements;


    public frontend_koan_KoanRule(
    ) {
        super(
        );
        this.statements = new ArrayList<>();
    }

    public frontend_koan_KoanRule(
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