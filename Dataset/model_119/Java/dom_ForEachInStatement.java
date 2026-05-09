





import java.util.List;
import java.util.ArrayList;

public class dom_ForEachInStatement extends IterationStatement {






    private dom_IForInitializer dom_iforinitializer;




    private dom_Expression dom_expression;


    public dom_ForEachInStatement(
    ) {
        super(
        );
    }



    public dom_IForInitializer getDom_iforinitializer() {
        return dom_iforinitializer;
    }

    public void setDom_iforinitializer(dom_IForInitializer dom_iforinitializer) {
        this.dom_iforinitializer = dom_iforinitializer;
    }
    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}