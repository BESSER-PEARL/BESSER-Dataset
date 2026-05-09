





import java.util.List;
import java.util.ArrayList;

public class dom_PropertyAccessExpression extends Expression {






    private dom_IProperty dom_iproperty;




    private dom_Expression dom_expression;


    public dom_PropertyAccessExpression(
    ) {
        super(
        );
    }



    public dom_IProperty getDom_iproperty() {
        return dom_iproperty;
    }

    public void setDom_iproperty(dom_IProperty dom_iproperty) {
        this.dom_iproperty = dom_iproperty;
    }
    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}