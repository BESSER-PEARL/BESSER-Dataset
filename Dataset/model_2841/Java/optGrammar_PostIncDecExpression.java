





import java.util.List;
import java.util.ArrayList;

public class optGrammar_PostIncDecExpression extends Expression {

    private String postOp;





    private optGrammar_Expression optgrammar_expression;


    public optGrammar_PostIncDecExpression(
        String postOp    ) {
        super(
        );
        this.postOp = postOp;
    }


    public String getPostop() {
        return postOp;
    }

    public void setPostop(String postOp) {
        this.postOp = postOp;
    }

    public optGrammar_Expression getOptgrammar_expression() {
        return optgrammar_expression;
    }

    public void setOptgrammar_expression(optGrammar_Expression optgrammar_expression) {
        this.optgrammar_expression = optgrammar_expression;
    }

}