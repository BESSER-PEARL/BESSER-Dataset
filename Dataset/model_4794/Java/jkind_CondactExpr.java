





import java.util.List;
import java.util.ArrayList;

public class jkind_CondactExpr extends Expr {






    private jkind_Expr jkind_expr;




    private jkind_CallExpr jkind_callexpr;




    private List<jkind_Expr> jkind_exprs;


    public jkind_CondactExpr(
    ) {
        super(
        );
        this.jkind_exprs = new ArrayList<>();
    }

    public jkind_CondactExpr(
        ArrayList<jkind_Expr> jkind_exprs    ) {
        this.jkind_exprs = jkind_exprs;
    }


    public jkind_Expr getJkind_expr() {
        return jkind_expr;
    }

    public void setJkind_expr(jkind_Expr jkind_expr) {
        this.jkind_expr = jkind_expr;
    }
    public jkind_CallExpr getJkind_callexpr() {
        return jkind_callexpr;
    }

    public void setJkind_callexpr(jkind_CallExpr jkind_callexpr) {
        this.jkind_callexpr = jkind_callexpr;
    }
    public List<jkind_Expr> getJkind_exprs() {
        return jkind_exprs;
    }

    public void addJkind_expr(Jkind_expr jkind_expr) {
        this.jkind_exprs.add(jkind_expr);
    }

}