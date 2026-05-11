





import java.util.List;
import java.util.ArrayList;

public class C_Expressions_DisplacementLogicExpression extends LogicExpression {

    private String operator;





    private Expressions_Expression expressions_expression;


    public C_Expressions_DisplacementLogicExpression(
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

    public Expressions_Expression getExpressions_expression() {
        return expressions_expression;
    }

    public void setExpressions_expression(Expressions_Expression expressions_expression) {
        this.expressions_expression = expressions_expression;
    }

}