





import java.util.List;
import java.util.ArrayList;

public class astm_sastm_RDBTrigger extends gastm_Definition, gastm_OtherSyntaxObject {






    private List<Statement> statements;


    public astm_sastm_RDBTrigger(
    ) {
        super(
        );
        this.statements = new ArrayList<>();
    }

    public astm_sastm_RDBTrigger(
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