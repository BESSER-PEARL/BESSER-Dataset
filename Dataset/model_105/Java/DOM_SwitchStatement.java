





import java.util.List;
import java.util.ArrayList;

public class DOM_SwitchStatement extends Statement {






    private List<DOM_Statement> dom_statements;




    private DOM_Expression dom_expression;


    public DOM_SwitchStatement(
    ) {
        super(
        );
        this.dom_statements = new ArrayList<>();
    }

    public DOM_SwitchStatement(
        ArrayList<DOM_Statement> dom_statements    ) {
        this.dom_statements = dom_statements;
    }


    public List<DOM_Statement> getDom_statements() {
        return dom_statements;
    }

    public void addDom_statement(Dom_statement dom_statement) {
        this.dom_statements.add(dom_statement);
    }
    public DOM_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(DOM_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}