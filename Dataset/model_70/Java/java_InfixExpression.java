





import java.util.List;
import java.util.ArrayList;

public class java_InfixExpression extends Expression {

    private String operator;





    private java_Expression java_expression;




    private java_Expression java_expression;




    private List<java_Expression> java_expressions;


    public java_InfixExpression(
        String operator    ) {
        super(
        );
        this.operator = operator;
        this.java_expressions = new ArrayList<>();
    }

    public java_InfixExpression(
        String operator        ArrayList<java_Expression> java_expressions    ) {
        this.operator = operator;
        this.java_expressions = java_expressions;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(java_Expression java_expression) {
        this.java_expression = java_expression;
    }
    public java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(java_Expression java_expression) {
        this.java_expression = java_expression;
    }
    public List<java_Expression> getJava_expressions() {
        return java_expressions;
    }

    public void addJava_expression(Java_expression java_expression) {
        this.java_expressions.add(java_expression);
    }

}