





import java.util.List;
import java.util.ArrayList;

public class dom_BlockStatement extends Statement {






    private dom_FunctionExpression dom_functionexpression;




    private dom_CatchClause dom_catchclause;




    private List<dom_Statement> dom_statements;




    private dom_FinallyClause dom_finallyclause;




    private dom_AccessorAssignment dom_accessorassignment;


    public dom_BlockStatement(
    ) {
        super(
        );
        this.dom_statements = new ArrayList<>();
    }

    public dom_BlockStatement(
        ArrayList<dom_Statement> dom_statements    ) {
        this.dom_statements = dom_statements;
    }


    public dom_FunctionExpression getDom_functionexpression() {
        return dom_functionexpression;
    }

    public void setDom_functionexpression(dom_FunctionExpression dom_functionexpression) {
        this.dom_functionexpression = dom_functionexpression;
    }
    public dom_CatchClause getDom_catchclause() {
        return dom_catchclause;
    }

    public void setDom_catchclause(dom_CatchClause dom_catchclause) {
        this.dom_catchclause = dom_catchclause;
    }
    public List<dom_Statement> getDom_statements() {
        return dom_statements;
    }

    public void addDom_statement(Dom_statement dom_statement) {
        this.dom_statements.add(dom_statement);
    }
    public dom_FinallyClause getDom_finallyclause() {
        return dom_finallyclause;
    }

    public void setDom_finallyclause(dom_FinallyClause dom_finallyclause) {
        this.dom_finallyclause = dom_finallyclause;
    }
    public dom_AccessorAssignment getDom_accessorassignment() {
        return dom_accessorassignment;
    }

    public void setDom_accessorassignment(dom_AccessorAssignment dom_accessorassignment) {
        this.dom_accessorassignment = dom_accessorassignment;
    }

}