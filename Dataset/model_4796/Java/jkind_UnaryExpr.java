





import java.util.List;
import java.util.ArrayList;

public class jkind_UnaryExpr extends Expr {

    private String op;





    private jkind_Expr jkind_expr;


    public jkind_UnaryExpr(
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

    public jkind_Expr getJkind_expr() {
        return jkind_expr;
    }

    public void setJkind_expr(jkind_Expr jkind_expr) {
        this.jkind_expr = jkind_expr;
    }

}