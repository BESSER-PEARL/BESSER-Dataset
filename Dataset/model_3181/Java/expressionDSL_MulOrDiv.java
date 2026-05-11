





import java.util.List;
import java.util.ArrayList;

public class expressionDSL_MulOrDiv extends Expression {

    private String op;





    private expressionDSL_Expression expressiondsl_expression;




    private expressionDSL_Expression expressiondsl_expression;


    public expressionDSL_MulOrDiv(
        String op    ) {
        super(
        );
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public expressionDSL_Expression getExpressiondsl_expression() {
        return expressiondsl_expression;
    }

    public void setExpressiondsl_expression(expressionDSL_Expression expressiondsl_expression) {
        this.expressiondsl_expression = expressiondsl_expression;
    }
    public expressionDSL_Expression getExpressiondsl_expression() {
        return expressiondsl_expression;
    }

    public void setExpressiondsl_expression(expressionDSL_Expression expressiondsl_expression) {
        this.expressiondsl_expression = expressiondsl_expression;
    }

}