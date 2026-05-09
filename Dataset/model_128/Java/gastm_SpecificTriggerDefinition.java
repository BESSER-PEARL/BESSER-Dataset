





import java.util.List;
import java.util.ArrayList;

public class gastm_SpecificTriggerDefinition extends Definition {






    private List<Statement> statements;


    public gastm_SpecificTriggerDefinition(
    ) {
        super(
        );
        this.statements = new ArrayList<>();
    }

    public gastm_SpecificTriggerDefinition(
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