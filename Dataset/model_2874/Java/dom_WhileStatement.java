





import java.util.List;
import java.util.ArrayList;

public class dom_WhileStatement extends Statement {






    private dom_Expression dom_expression;




    private dom_Block dom_block;


    public dom_WhileStatement(
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
    public dom_Block getDom_block() {
        return dom_block;
    }

    public void setDom_block(dom_Block dom_block) {
        this.dom_block = dom_block;
    }

}