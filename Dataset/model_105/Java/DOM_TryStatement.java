





import java.util.List;
import java.util.ArrayList;

public class DOM_TryStatement extends Statement {






    private DOM_Block dom_block;




    private List<DOM_CatchClause> dom_catchclauses;




    private DOM_Block dom_block;


    public DOM_TryStatement(
    ) {
        super(
        );
        this.dom_catchclauses = new ArrayList<>();
    }

    public DOM_TryStatement(
        ArrayList<DOM_CatchClause> dom_catchclauses    ) {
        this.dom_catchclauses = dom_catchclauses;
    }


    public DOM_Block getDom_block() {
        return dom_block;
    }

    public void setDom_block(DOM_Block dom_block) {
        this.dom_block = dom_block;
    }
    public List<DOM_CatchClause> getDom_catchclauses() {
        return dom_catchclauses;
    }

    public void addDom_catchclause(Dom_catchclause dom_catchclause) {
        this.dom_catchclauses.add(dom_catchclause);
    }
    public DOM_Block getDom_block() {
        return dom_block;
    }

    public void setDom_block(DOM_Block dom_block) {
        this.dom_block = dom_block;
    }

}