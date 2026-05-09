





import java.util.List;
import java.util.ArrayList;

public class DOM_CastExpression extends Expression {






    private DOM_Expression dom_expression;




    private DOM_Type dom_type;


    public DOM_CastExpression(
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
    public DOM_Type getDom_type() {
        return dom_type;
    }

    public void setDom_type(DOM_Type dom_type) {
        this.dom_type = dom_type;
    }

}