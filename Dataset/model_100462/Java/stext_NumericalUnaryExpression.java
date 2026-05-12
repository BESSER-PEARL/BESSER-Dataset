





import java.util.List;
import java.util.ArrayList;

public class stext_NumericalUnaryExpression extends Expression {

    private String operator;





    private stext_Expression stext_expression;


    public stext_NumericalUnaryExpression(
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

    public stext_Expression getStext_expression() {
        return stext_expression;
    }

    public void setStext_expression(stext_Expression stext_expression) {
        this.stext_expression = stext_expression;
    }

}