





import java.util.List;
import java.util.ArrayList;

public class xs_ForStatement extends Statement {

    private String op;





    private xs_ForVarDeclaration xs_forvardeclaration;




    private xs_Expression xs_expression;


    public xs_ForStatement(
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

    public xs_ForVarDeclaration getXs_forvardeclaration() {
        return xs_forvardeclaration;
    }

    public void setXs_forvardeclaration(xs_ForVarDeclaration xs_forvardeclaration) {
        this.xs_forvardeclaration = xs_forvardeclaration;
    }
    public xs_Expression getXs_expression() {
        return xs_expression;
    }

    public void setXs_expression(xs_Expression xs_expression) {
        this.xs_expression = xs_expression;
    }

}