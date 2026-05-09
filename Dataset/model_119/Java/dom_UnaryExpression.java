





import java.util.List;
import java.util.ArrayList;

public class dom_UnaryExpression extends Expression {

    private String operation;





    private dom_Expression dom_expression;


    public dom_UnaryExpression(
        String operation    ) {
        super(
        );
        this.operation = operation;
    }


    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }

    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}