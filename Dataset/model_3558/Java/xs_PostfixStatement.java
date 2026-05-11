





import java.util.List;
import java.util.ArrayList;

public class xs_PostfixStatement extends Statement {

    private String op;





    private xs_VarDeclaration xs_vardeclaration;


    public xs_PostfixStatement(
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

    public xs_VarDeclaration getXs_vardeclaration() {
        return xs_vardeclaration;
    }

    public void setXs_vardeclaration(xs_VarDeclaration xs_vardeclaration) {
        this.xs_vardeclaration = xs_vardeclaration;
    }

}