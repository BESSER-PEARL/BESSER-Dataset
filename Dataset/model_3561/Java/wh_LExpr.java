





import java.util.List;
import java.util.ArrayList;

public class wh_LExpr  {






    private List<wh_Expr> wh_exprs;


    public wh_LExpr(
    ) {
        this.wh_exprs = new ArrayList<>();
    }

    public wh_LExpr(
        ArrayList<wh_Expr> wh_exprs    ) {
        this.wh_exprs = wh_exprs;
    }


    public List<wh_Expr> getWh_exprs() {
        return wh_exprs;
    }

    public void addWh_expr(Wh_expr wh_expr) {
        this.wh_exprs.add(wh_expr);
    }

}