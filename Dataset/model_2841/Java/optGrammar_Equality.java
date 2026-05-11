





import java.util.List;
import java.util.ArrayList;

public class optGrammar_Equality extends Expression {

    private String equalityOp;





    private optGrammar_Expression optgrammar_expression;




    private optGrammar_Expression optgrammar_expression;


    public optGrammar_Equality(
        String equalityOp    ) {
        super(
        );
        this.equalityOp = equalityOp;
    }


    public String getEqualityop() {
        return equalityOp;
    }

    public void setEqualityop(String equalityOp) {
        this.equalityOp = equalityOp;
    }

    public optGrammar_Expression getOptgrammar_expression() {
        return optgrammar_expression;
    }

    public void setOptgrammar_expression(optGrammar_Expression optgrammar_expression) {
        this.optgrammar_expression = optgrammar_expression;
    }
    public optGrammar_Expression getOptgrammar_expression() {
        return optgrammar_expression;
    }

    public void setOptgrammar_expression(optGrammar_Expression optgrammar_expression) {
        this.optgrammar_expression = optgrammar_expression;
    }

}