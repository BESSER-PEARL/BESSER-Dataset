





import java.util.List;
import java.util.ArrayList;

public class aDSL_MulOrDiv extends Expression {

    private String op;





    private aDSL_Expression adsl_expression;




    private aDSL_Expression adsl_expression;


    public aDSL_MulOrDiv(
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

    public aDSL_Expression getAdsl_expression() {
        return adsl_expression;
    }

    public void setAdsl_expression(aDSL_Expression adsl_expression) {
        this.adsl_expression = adsl_expression;
    }
    public aDSL_Expression getAdsl_expression() {
        return adsl_expression;
    }

    public void setAdsl_expression(aDSL_Expression adsl_expression) {
        this.adsl_expression = adsl_expression;
    }

}