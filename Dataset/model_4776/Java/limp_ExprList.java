





import java.util.List;
import java.util.ArrayList;

public class limp_ExprList  {






    private List<limp_Expr> limp_exprs;




    private limp_FcnCallExpr limp_fcncallexpr;


    public limp_ExprList(
    ) {
        this.limp_exprs = new ArrayList<>();
    }

    public limp_ExprList(
        ArrayList<limp_Expr> limp_exprs    ) {
        this.limp_exprs = limp_exprs;
    }


    public List<limp_Expr> getLimp_exprs() {
        return limp_exprs;
    }

    public void addLimp_expr(Limp_expr limp_expr) {
        this.limp_exprs.add(limp_expr);
    }
    public limp_FcnCallExpr getLimp_fcncallexpr() {
        return limp_fcncallexpr;
    }

    public void setLimp_fcncallexpr(limp_FcnCallExpr limp_fcncallexpr) {
        this.limp_fcncallexpr = limp_fcncallexpr;
    }

}