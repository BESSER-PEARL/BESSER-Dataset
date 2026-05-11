





import java.util.List;
import java.util.ArrayList;

public class jkind_ArrayUpdateExpr extends Expr {






    private jkind_ArrayAccessExpr jkind_arrayaccessexpr;




    private jkind_Expr jkind_expr;


    public jkind_ArrayUpdateExpr(
    ) {
        super(
        );
    }



    public jkind_ArrayAccessExpr getJkind_arrayaccessexpr() {
        return jkind_arrayaccessexpr;
    }

    public void setJkind_arrayaccessexpr(jkind_ArrayAccessExpr jkind_arrayaccessexpr) {
        this.jkind_arrayaccessexpr = jkind_arrayaccessexpr;
    }
    public jkind_Expr getJkind_expr() {
        return jkind_expr;
    }

    public void setJkind_expr(jkind_Expr jkind_expr) {
        this.jkind_expr = jkind_expr;
    }

}