





import java.util.List;
import java.util.ArrayList;

public class dom_TryStatement extends Statement {






    private List<dom_CatchClause> dom_catchclauses;




    private dom_FinallyClause dom_finallyclause;




    private dom_BlockStatement dom_blockstatement;


    public dom_TryStatement(
    ) {
        super(
        );
        this.dom_catchclauses = new ArrayList<>();
    }

    public dom_TryStatement(
        ArrayList<dom_CatchClause> dom_catchclauses    ) {
        this.dom_catchclauses = dom_catchclauses;
    }


    public List<dom_CatchClause> getDom_catchclauses() {
        return dom_catchclauses;
    }

    public void addDom_catchclause(Dom_catchclause dom_catchclause) {
        this.dom_catchclauses.add(dom_catchclause);
    }
    public dom_FinallyClause getDom_finallyclause() {
        return dom_finallyclause;
    }

    public void setDom_finallyclause(dom_FinallyClause dom_finallyclause) {
        this.dom_finallyclause = dom_finallyclause;
    }
    public dom_BlockStatement getDom_blockstatement() {
        return dom_blockstatement;
    }

    public void setDom_blockstatement(dom_BlockStatement dom_blockstatement) {
        this.dom_blockstatement = dom_blockstatement;
    }

}