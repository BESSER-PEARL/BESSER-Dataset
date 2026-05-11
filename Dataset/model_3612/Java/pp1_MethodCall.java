





import java.util.List;
import java.util.ArrayList;

public class pp1_MethodCall extends WithLambdaExpression {

    private boolean parenthesized;





    private pp1_Expression pp1_expression;


    public pp1_MethodCall(
        boolean parenthesized    ) {
        super(
        );
        this.parenthesized = parenthesized;
    }


    public boolean getParenthesized() {
        return parenthesized;
    }

    public void setParenthesized(boolean parenthesized) {
        this.parenthesized = parenthesized;
    }

    public pp1_Expression getPp1_expression() {
        return pp1_expression;
    }

    public void setPp1_expression(pp1_Expression pp1_expression) {
        this.pp1_expression = pp1_expression;
    }

}