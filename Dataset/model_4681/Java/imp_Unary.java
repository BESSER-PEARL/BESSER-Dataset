





import java.util.List;
import java.util.ArrayList;

public class imp_Unary extends Expr {

    private String op;





    private imp_Expr imp_expr;


    public imp_Unary(
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

    public imp_Expr getImp_expr() {
        return imp_expr;
    }

    public void setImp_expr(imp_Expr imp_expr) {
        this.imp_expr = imp_expr;
    }

}