





import java.util.List;
import java.util.ArrayList;

public class dom_CatchClause extends Node {






    private dom_Identifier dom_identifier;




    private dom_Expression dom_expression;


    public dom_CatchClause(
    ) {
        super(
        );
    }



    public dom_Identifier getDom_identifier() {
        return dom_identifier;
    }

    public void setDom_identifier(dom_Identifier dom_identifier) {
        this.dom_identifier = dom_identifier;
    }
    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}