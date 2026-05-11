





import java.util.List;
import java.util.ArrayList;

public class pp2_MethodCall extends WithLambdaExpression {

    private boolean parenthesized;





    private pp2_Expression pp2_expression;


    public pp2_MethodCall(
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

    public pp2_Expression getPp2_expression() {
        return pp2_expression;
    }

    public void setPp2_expression(pp2_Expression pp2_expression) {
        this.pp2_expression = pp2_expression;
    }

}