





import java.util.List;
import java.util.ArrayList;

public class DOM_SynchronizedStatement extends Statement {






    private DOM_Block dom_block;




    private DOM_Expression dom_expression;


    public DOM_SynchronizedStatement(
    ) {
        super(
        );
    }



    public DOM_Block getDom_block() {
        return dom_block;
    }

    public void setDom_block(DOM_Block dom_block) {
        this.dom_block = dom_block;
    }
    public DOM_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(DOM_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}