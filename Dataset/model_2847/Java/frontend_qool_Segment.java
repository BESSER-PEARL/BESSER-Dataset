





import java.util.List;
import java.util.ArrayList;

public class frontend_qool_Segment extends NamedElement {






    private List<Statement> statements;


    public frontend_qool_Segment(
    ) {
        super(
        );
        this.statements = new ArrayList<>();
    }

    public frontend_qool_Segment(
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