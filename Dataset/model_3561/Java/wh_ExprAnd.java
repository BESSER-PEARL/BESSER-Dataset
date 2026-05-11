





import java.util.List;
import java.util.ArrayList;

public class wh_ExprAnd  {






    private List<wh_ExprOr> wh_exprors;




    private wh_Expr wh_expr;


    public wh_ExprAnd(
    ) {
        this.wh_exprors = new ArrayList<>();
    }

    public wh_ExprAnd(
        ArrayList<wh_ExprOr> wh_exprors    ) {
        this.wh_exprors = wh_exprors;
    }


    public List<wh_ExprOr> getWh_exprors() {
        return wh_exprors;
    }

    public void addWh_expror(Wh_expror wh_expror) {
        this.wh_exprors.add(wh_expror);
    }
    public wh_Expr getWh_expr() {
        return wh_expr;
    }

    public void setWh_expr(wh_Expr wh_expr) {
        this.wh_expr = wh_expr;
    }

}