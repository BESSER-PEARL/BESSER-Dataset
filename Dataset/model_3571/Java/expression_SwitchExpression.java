





import java.util.List;
import java.util.ArrayList;

public class expression_SwitchExpression extends Expression {






    private List<expression_Case> expression_cases;




    private expression_Expression expression_expression;




    private expression_Expression expression_expression;


    public expression_SwitchExpression(
    ) {
        super(
        );
        this.expression_cases = new ArrayList<>();
    }

    public expression_SwitchExpression(
        ArrayList<expression_Case> expression_cases    ) {
        this.expression_cases = expression_cases;
    }


    public List<expression_Case> getExpression_cases() {
        return expression_cases;
    }

    public void addExpression_case(Expression_case expression_case) {
        this.expression_cases.add(expression_case);
    }
    public expression_Expression getExpression_expression() {
        return expression_expression;
    }

    public void setExpression_expression(expression_Expression expression_expression) {
        this.expression_expression = expression_expression;
    }
    public expression_Expression getExpression_expression() {
        return expression_expression;
    }

    public void setExpression_expression(expression_Expression expression_expression) {
        this.expression_expression = expression_expression;
    }

}