





import java.util.List;
import java.util.ArrayList;

public class DOM_Block extends Statement {






    private DOM_CatchClause dom_catchclause;




    private List<DOM_Statement> dom_statements;


    public DOM_Block(
    ) {
        super(
        );
        this.dom_statements = new ArrayList<>();
    }

    public DOM_Block(
        ArrayList<DOM_Statement> dom_statements    ) {
        this.dom_statements = dom_statements;
    }


    public DOM_CatchClause getDom_catchclause() {
        return dom_catchclause;
    }

    public void setDom_catchclause(DOM_CatchClause dom_catchclause) {
        this.dom_catchclause = dom_catchclause;
    }
    public List<DOM_Statement> getDom_statements() {
        return dom_statements;
    }

    public void addDom_statement(Dom_statement dom_statement) {
        this.dom_statements.add(dom_statement);
    }

}