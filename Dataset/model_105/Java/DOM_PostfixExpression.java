





import java.util.List;
import java.util.ArrayList;

public class DOM_PostfixExpression extends Expression {

    private String operator;





    private DOM_Expression dom_expression;


    public DOM_PostfixExpression(
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

    public DOM_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(DOM_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}