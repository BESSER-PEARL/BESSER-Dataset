





import java.util.List;
import java.util.ArrayList;

public class Java_InfixExpression extends Expression {

    private String operator;





    private Java_Expression java_expression;




    private List<Java_Expression> java_expressions;




    private Java_Expression java_expression;


    public Java_InfixExpression(
        String operator    ) {
        super(
        );
        this.operator = operator;
        this.java_expressions = new ArrayList<>();
    }

    public Java_InfixExpression(
        String operator        ArrayList<Java_Expression> java_expressions    ) {
        this.operator = operator;
        this.java_expressions = java_expressions;
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
    public List<Java_Expression> getJava_expressions() {
        return java_expressions;
    }

    public void addJava_expression(Java_expression java_expression) {
        this.java_expressions.add(java_expression);
    }
    public Java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(Java_Expression java_expression) {
        this.java_expression = java_expression;
    }

}