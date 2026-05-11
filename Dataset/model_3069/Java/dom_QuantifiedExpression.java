





import java.util.List;
import java.util.ArrayList;

public class dom_QuantifiedExpression extends Expression {

    private String quantifier;
    private String name;





    private dom_Expression dom_expression;


    public dom_QuantifiedExpression(
        String quantifier,        String name    ) {
        super(
        );
        this.quantifier = quantifier;
        this.name = name;
    }


    public String getQuantifier() {
        return quantifier;
    }

    public void setQuantifier(String quantifier) {
        this.quantifier = quantifier;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}