





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_expressions_WithArgumentsExpression extends Expression {






    private List<expressions_Expression> expressions_expressions;




    private expressions_Expression expressions_expression;


    public timedAutomata_expressions_WithArgumentsExpression(
    ) {
        super(
        );
        this.expressions_expressions = new ArrayList<>();
    }

    public timedAutomata_expressions_WithArgumentsExpression(
        ArrayList<expressions_Expression> expressions_expressions    ) {
        this.expressions_expressions = expressions_expressions;
    }


    public List<expressions_Expression> getExpressions_expressions() {
        return expressions_expressions;
    }

    public void addExpressions_expression(Expressions_expression expressions_expression) {
        this.expressions_expressions.add(expressions_expression);
    }
    public expressions_Expression getExpressions_expression() {
        return expressions_expression;
    }

    public void setExpressions_expression(expressions_Expression expressions_expression) {
        this.expressions_expression = expressions_expression;
    }

}