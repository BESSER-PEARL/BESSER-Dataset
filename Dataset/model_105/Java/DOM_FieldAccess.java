





import java.util.List;
import java.util.ArrayList;

public class DOM_FieldAccess extends Expression {






    private DOM_SimpleName dom_simplename;




    private DOM_Expression dom_expression;


    public DOM_FieldAccess(
    ) {
        super(
        );
    }



    public DOM_SimpleName getDom_simplename() {
        return dom_simplename;
    }

    public void setDom_simplename(DOM_SimpleName dom_simplename) {
        this.dom_simplename = dom_simplename;
    }
    public DOM_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(DOM_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}