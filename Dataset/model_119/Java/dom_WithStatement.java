





import java.util.List;
import java.util.ArrayList;

public class dom_WithStatement extends Statement {






    private dom_Expression dom_expression;




    private dom_Statement dom_statement;


    public dom_WithStatement(
    ) {
        super(
        );
    }



    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }
    public dom_Statement getDom_statement() {
        return dom_statement;
    }

    public void setDom_statement(dom_Statement dom_statement) {
        this.dom_statement = dom_statement;
    }

}