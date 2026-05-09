





import java.util.List;
import java.util.ArrayList;

public class astm_gastm_SpecificTriggerDefinition extends Definition {






    private List<Statement> statements;


    public astm_gastm_SpecificTriggerDefinition(
    ) {
        super(
        );
        this.statements = new ArrayList<>();
    }

    public astm_gastm_SpecificTriggerDefinition(
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