





import java.util.List;
import java.util.ArrayList;

public class optGrammar_Shift extends Expression {

    private String shiftOp;





    private optGrammar_Expression optgrammar_expression;




    private optGrammar_Expression optgrammar_expression;


    public optGrammar_Shift(
        String shiftOp    ) {
        super(
        );
        this.shiftOp = shiftOp;
    }


    public String getShiftop() {
        return shiftOp;
    }

    public void setShiftop(String shiftOp) {
        this.shiftOp = shiftOp;
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