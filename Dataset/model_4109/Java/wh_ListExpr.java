





import java.util.List;
import java.util.ArrayList;

public class wh_ListExpr  {






    private List<wh_Expr> wh_exprs;




    private wh_Cons wh_cons;




    private wh_ExprSimple wh_exprsimple;


    public wh_ListExpr(
    ) {
        this.wh_exprs = new ArrayList<>();
    }

    public wh_ListExpr(
        ArrayList<wh_Expr> wh_exprs    ) {
        this.wh_exprs = wh_exprs;
    }


    public List<wh_Expr> getWh_exprs() {
        return wh_exprs;
    }

    public void addWh_expr(Wh_expr wh_expr) {
        this.wh_exprs.add(wh_expr);
    }
    public wh_Cons getWh_cons() {
        return wh_cons;
    }

    public void setWh_cons(wh_Cons wh_cons) {
        this.wh_cons = wh_cons;
    }
    public wh_ExprSimple getWh_exprsimple() {
        return wh_exprsimple;
    }

    public void setWh_exprsimple(wh_ExprSimple wh_exprsimple) {
        this.wh_exprsimple = wh_exprsimple;
    }

}