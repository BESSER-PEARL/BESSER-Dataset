





import java.util.List;
import java.util.ArrayList;

public class behaviour_LoopStatement extends Statement {






    private List<behaviour_Statement> behaviour_statements;


    public behaviour_LoopStatement(
    ) {
        super(
        );
        this.behaviour_statements = new ArrayList<>();
    }

    public behaviour_LoopStatement(
        ArrayList<behaviour_Statement> behaviour_statements    ) {
        this.behaviour_statements = behaviour_statements;
    }


    public List<behaviour_Statement> getBehaviour_statements() {
        return behaviour_statements;
    }

    public void addBehaviour_statement(Behaviour_statement behaviour_statement) {
        this.behaviour_statements.add(behaviour_statement);
    }

}