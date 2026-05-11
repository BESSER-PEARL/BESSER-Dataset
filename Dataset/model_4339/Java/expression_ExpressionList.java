





import java.util.List;
import java.util.ArrayList;

public class expression_ExpressionList  {






    private expression_FunctionCall expression_functioncall;




    private expression_Expression expression_expression;




    private List<expression_ExpressionRest> expression_expressionrests;


    public expression_ExpressionList(
    ) {
        this.expression_expressionrests = new ArrayList<>();
    }

    public expression_ExpressionList(
        ArrayList<expression_ExpressionRest> expression_expressionrests    ) {
        this.expression_expressionrests = expression_expressionrests;
    }


    public expression_FunctionCall getExpression_functioncall() {
        return expression_functioncall;
    }

    public void setExpression_functioncall(expression_FunctionCall expression_functioncall) {
        this.expression_functioncall = expression_functioncall;
    }
    public expression_Expression getExpression_expression() {
        return expression_expression;
    }

    public void setExpression_expression(expression_Expression expression_expression) {
        this.expression_expression = expression_expression;
    }
    public List<expression_ExpressionRest> getExpression_expressionrests() {
        return expression_expressionrests;
    }

    public void addExpression_expressionrest(Expression_expressionrest expression_expressionrest) {
        this.expression_expressionrests.add(expression_expressionrest);
    }

}