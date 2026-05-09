





import java.util.List;
import java.util.ArrayList;

public class javaMM_InfixExpression extends Expression {

    private String operator;





    private javaMM_Expression javamm_expression;




    private javaMM_Expression javamm_expression;




    private List<javaMM_Expression> javamm_expressions;


    public javaMM_InfixExpression(
        String operator    ) {
        super(
        );
        this.operator = operator;
        this.javamm_expressions = new ArrayList<>();
    }

    public javaMM_InfixExpression(
        String operator        ArrayList<javaMM_Expression> javamm_expressions    ) {
        this.operator = operator;
        this.javamm_expressions = javamm_expressions;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public javaMM_Expression getJavamm_expression() {
        return javamm_expression;
    }

    public void setJavamm_expression(javaMM_Expression javamm_expression) {
        this.javamm_expression = javamm_expression;
    }
    public javaMM_Expression getJavamm_expression() {
        return javamm_expression;
    }

    public void setJavamm_expression(javaMM_Expression javamm_expression) {
        this.javamm_expression = javamm_expression;
    }
    public List<javaMM_Expression> getJavamm_expressions() {
        return javamm_expressions;
    }

    public void addJavamm_expression(Javamm_expression javamm_expression) {
        this.javamm_expressions.add(javamm_expression);
    }

}