





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_expressions_IncDecExpression extends Expression {

    private boolean increment;
    private boolean beforeExpression;





    private expressions_Expression expressions_expression;


    public timedAutomata_expressions_IncDecExpression(
        boolean increment,        boolean beforeExpression    ) {
        super(
        );
        this.increment = increment;
        this.beforeExpression = beforeExpression;
    }


    public boolean getIncrement() {
        return increment;
    }

    public void setIncrement(boolean increment) {
        this.increment = increment;
    }
    public boolean getBeforeexpression() {
        return beforeExpression;
    }

    public void setBeforeexpression(boolean beforeExpression) {
        this.beforeExpression = beforeExpression;
    }

    public expressions_Expression getExpressions_expression() {
        return expressions_expression;
    }

    public void setExpressions_expression(expressions_Expression expressions_expression) {
        this.expressions_expression = expressions_expression;
    }

}