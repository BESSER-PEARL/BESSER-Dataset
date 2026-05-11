





import java.util.List;
import java.util.ArrayList;

public class wh_ExprAnd extends Expr {






    private wh_ExprSimple wh_exprsimple;




    private wh_Expr wh_expr;


    public wh_ExprAnd(
    ) {
        super(
        );
    }



    public wh_ExprSimple getWh_exprsimple() {
        return wh_exprsimple;
    }

    public void setWh_exprsimple(wh_ExprSimple wh_exprsimple) {
        this.wh_exprsimple = wh_exprsimple;
    }
    public wh_Expr getWh_expr() {
        return wh_expr;
    }

    public void setWh_expr(wh_Expr wh_expr) {
        this.wh_expr = wh_expr;
    }

}