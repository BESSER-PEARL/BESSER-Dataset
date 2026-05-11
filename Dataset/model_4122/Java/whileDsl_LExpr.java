





import java.util.List;
import java.util.ArrayList;

public class whileDsl_LExpr  {






    private whileDsl_ExprSimpleWithLExpr whiledsl_exprsimplewithlexpr;




    private List<whileDsl_Expr> whiledsl_exprs;


    public whileDsl_LExpr(
    ) {
        this.whiledsl_exprs = new ArrayList<>();
    }

    public whileDsl_LExpr(
        ArrayList<whileDsl_Expr> whiledsl_exprs    ) {
        this.whiledsl_exprs = whiledsl_exprs;
    }


    public whileDsl_ExprSimpleWithLExpr getWhiledsl_exprsimplewithlexpr() {
        return whiledsl_exprsimplewithlexpr;
    }

    public void setWhiledsl_exprsimplewithlexpr(whileDsl_ExprSimpleWithLExpr whiledsl_exprsimplewithlexpr) {
        this.whiledsl_exprsimplewithlexpr = whiledsl_exprsimplewithlexpr;
    }
    public List<whileDsl_Expr> getWhiledsl_exprs() {
        return whiledsl_exprs;
    }

    public void addWhiledsl_expr(Whiledsl_expr whiledsl_expr) {
        this.whiledsl_exprs.add(whiledsl_expr);
    }

}