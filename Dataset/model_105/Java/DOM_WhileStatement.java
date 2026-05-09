





import java.util.List;
import java.util.ArrayList;

public class DOM_WhileStatement extends Statement {






    private DOM_Expression dom_expression;




    private DOM_Statement dom_statement;


    public DOM_WhileStatement(
    ) {
        super(
        );
    }



    public DOM_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(DOM_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }
    public DOM_Statement getDom_statement() {
        return dom_statement;
    }

    public void setDom_statement(DOM_Statement dom_statement) {
        this.dom_statement = dom_statement;
    }

}