





import java.util.List;
import java.util.ArrayList;

public class javaMM_TryStatement extends Statement {






    private List<javaMM_CatchClause> javamm_catchclauses;


    public javaMM_TryStatement(
    ) {
        super(
        );
        this.javamm_catchclauses = new ArrayList<>();
    }

    public javaMM_TryStatement(
        ArrayList<javaMM_CatchClause> javamm_catchclauses    ) {
        this.javamm_catchclauses = javamm_catchclauses;
    }


    public List<javaMM_CatchClause> getJavamm_catchclauses() {
        return javamm_catchclauses;
    }

    public void addJavamm_catchclause(Javamm_catchclause javamm_catchclause) {
        this.javamm_catchclauses.add(javamm_catchclause);
    }

}