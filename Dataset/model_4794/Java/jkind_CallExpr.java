





import java.util.List;
import java.util.ArrayList;

public class jkind_CallExpr extends Expr {






    private List<jkind_Expr> jkind_exprs;


    public jkind_CallExpr(
    ) {
        super(
        );
        this.jkind_exprs = new ArrayList<>();
    }

    public jkind_CallExpr(
        ArrayList<jkind_Expr> jkind_exprs    ) {
        this.jkind_exprs = jkind_exprs;
    }


    public List<jkind_Expr> getJkind_exprs() {
        return jkind_exprs;
    }

    public void addJkind_expr(Jkind_expr jkind_expr) {
        this.jkind_exprs.add(jkind_expr);
    }

}