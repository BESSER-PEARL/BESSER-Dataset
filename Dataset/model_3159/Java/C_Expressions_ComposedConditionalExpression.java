





import java.util.List;
import java.util.ArrayList;

public class C_Expressions_ComposedConditionalExpression extends ConditionalExpression {

    private String operator;





    private List<Expressions_Expression> expressions_expressions;


    public C_Expressions_ComposedConditionalExpression(
        String operator    ) {
        super(
        );
        this.operator = operator;
        this.expressions_expressions = new ArrayList<>();
    }

    public C_Expressions_ComposedConditionalExpression(
        String operator        ArrayList<Expressions_Expression> expressions_expressions    ) {
        this.operator = operator;
        this.expressions_expressions = expressions_expressions;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public List<Expressions_Expression> getExpressions_expressions() {
        return expressions_expressions;
    }

    public void addExpressions_expression(Expressions_expression expressions_expression) {
        this.expressions_expressions.add(expressions_expression);
    }

}