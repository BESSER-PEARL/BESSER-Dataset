





import java.util.List;
import java.util.ArrayList;

public class optGrammar_Comparison extends Expression {

    private String comparisonOp;





    private optGrammar_Expression optgrammar_expression;




    private optGrammar_Expression optgrammar_expression;


    public optGrammar_Comparison(
        String comparisonOp    ) {
        super(
        );
        this.comparisonOp = comparisonOp;
    }


    public String getComparisonop() {
        return comparisonOp;
    }

    public void setComparisonop(String comparisonOp) {
        this.comparisonOp = comparisonOp;
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