





import java.util.List;
import java.util.ArrayList;

public class dom_AliasedExpression extends Expression {

    private String name;





    private dom_Expression dom_expression;


    public dom_AliasedExpression(
        String name    ) {
        super(
        );
        this.name = name;
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