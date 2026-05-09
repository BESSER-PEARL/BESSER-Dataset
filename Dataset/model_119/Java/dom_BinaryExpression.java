





import java.util.List;
import java.util.ArrayList;

public class dom_BinaryExpression extends Expression {

    private int operatorPosition;
    private String operation;





    private dom_Expression dom_expression;




    private dom_Expression dom_expression;


    public dom_BinaryExpression(
        int operatorPosition,        String operation    ) {
        super(
        );
        this.operatorPosition = operatorPosition;
        this.operation = operation;
    }


    public int getOperatorposition() {
        return operatorPosition;
    }

    public void setOperatorposition(int operatorPosition) {
        this.operatorPosition = operatorPosition;
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
    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}