





import java.util.List;
import java.util.ArrayList;

public class pp_MethodCall extends WithLambdaExpression {

    private boolean parenthesized;





    private pp_Expression pp_expression;


    public pp_MethodCall(
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

    public pp_Expression getPp_expression() {
        return pp_expression;
    }

    public void setPp_expression(pp_Expression pp_expression) {
        this.pp_expression = pp_expression;
    }

}