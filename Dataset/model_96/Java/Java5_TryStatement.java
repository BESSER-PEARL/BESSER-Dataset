





import java.util.List;
import java.util.ArrayList;

public class Java5_TryStatement extends Statement {






    private List<Java5_CatchClause> java5_catchclauses;


    public Java5_TryStatement(
    ) {
        super(
        );
        this.java5_catchclauses = new ArrayList<>();
    }

    public Java5_TryStatement(
        ArrayList<Java5_CatchClause> java5_catchclauses    ) {
        this.java5_catchclauses = java5_catchclauses;
    }


    public List<Java5_CatchClause> getJava5_catchclauses() {
        return java5_catchclauses;
    }

    public void addJava5_catchclause(Java5_catchclause java5_catchclause) {
        this.java5_catchclauses.add(java5_catchclause);
    }

}