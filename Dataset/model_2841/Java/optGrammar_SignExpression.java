





import java.util.List;
import java.util.ArrayList;

public class optGrammar_SignExpression extends Expression {

    private String signOp;





    private optGrammar_Expression optgrammar_expression;


    public optGrammar_SignExpression(
        String signOp    ) {
        super(
        );
        this.signOp = signOp;
    }


    public String getSignop() {
        return signOp;
    }

    public void setSignop(String signOp) {
        this.signOp = signOp;
    }

    public optGrammar_Expression getOptgrammar_expression() {
        return optgrammar_expression;
    }

    public void setOptgrammar_expression(optGrammar_Expression optgrammar_expression) {
        this.optgrammar_expression = optgrammar_expression;
    }

}