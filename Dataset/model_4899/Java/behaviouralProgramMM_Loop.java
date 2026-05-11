





import java.util.List;
import java.util.ArrayList;

public class behaviouralProgramMM_Loop extends Statement {






    private List<behaviouralProgramMM_Statement> behaviouralprogrammm_statements;


    public behaviouralProgramMM_Loop(
    ) {
        super(
        );
        this.behaviouralprogrammm_statements = new ArrayList<>();
    }

    public behaviouralProgramMM_Loop(
        ArrayList<behaviouralProgramMM_Statement> behaviouralprogrammm_statements    ) {
        this.behaviouralprogrammm_statements = behaviouralprogrammm_statements;
    }


    public List<behaviouralProgramMM_Statement> getBehaviouralprogrammm_statements() {
        return behaviouralprogrammm_statements;
    }

    public void addBehaviouralprogrammm_statement(Behaviouralprogrammm_statement behaviouralprogrammm_statement) {
        this.behaviouralprogrammm_statements.add(behaviouralprogrammm_statement);
    }

}