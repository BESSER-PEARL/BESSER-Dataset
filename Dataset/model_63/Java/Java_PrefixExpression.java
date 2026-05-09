





import java.util.List;
import java.util.ArrayList;

public class Java_PrefixExpression extends Expression {

    private String operator;





    private Java_Expression java_expression;


    public Java_PrefixExpression(
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

    public Java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(Java_Expression java_expression) {
        this.java_expression = java_expression;
    }

}