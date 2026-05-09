





import java.util.List;
import java.util.ArrayList;

public class java__InfixExpression extends Expression {

    private String operator;





    private java__Expression java__expression;




    private List<java__Expression> java__expressions;




    private java__Expression java__expression;


    public java__InfixExpression(
        String operator    ) {
        super(
        );
        this.operator = operator;
        this.java__expressions = new ArrayList<>();
    }

    public java__InfixExpression(
        String operator        ArrayList<java__Expression> java__expressions    ) {
        this.operator = operator;
        this.java__expressions = java__expressions;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public java__Expression getJava__expression() {
        return java__expression;
    }

    public void setJava__expression(java__Expression java__expression) {
        this.java__expression = java__expression;
    }
    public List<java__Expression> getJava__expressions() {
        return java__expressions;
    }

    public void addJava__expression(Java__expression java__expression) {
        this.java__expressions.add(java__expression);
    }
    public java__Expression getJava__expression() {
        return java__expression;
    }

    public void setJava__expression(java__Expression java__expression) {
        this.java__expression = java__expression;
    }

}