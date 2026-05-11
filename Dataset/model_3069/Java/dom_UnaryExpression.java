





import java.util.List;
import java.util.ArrayList;

public class dom_UnaryExpression extends Expression {

    private String operator;





    private dom_Expression dom_expression;


    public dom_UnaryExpression(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}