





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_expressions_UnaryExpression extends Expression {

    private String operator;





    private expressions_Expression expressions_expression;


    public timedAutomata_expressions_UnaryExpression(
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

    public expressions_Expression getExpressions_expression() {
        return expressions_expression;
    }

    public void setExpressions_expression(expressions_Expression expressions_expression) {
        this.expressions_expression = expressions_expression;
    }

}