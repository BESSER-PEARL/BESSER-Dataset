





import java.util.List;
import java.util.ArrayList;

public class wh_Expr  {






    private wh_ExprOr wh_expror;




    private wh_Expr wh_expr;




    private wh_If wh_if;


    public wh_Expr(
    ) {
    }



    public wh_ExprOr getWh_expror() {
        return wh_expror;
    }

    public void setWh_expror(wh_ExprOr wh_expror) {
        this.wh_expror = wh_expror;
    }
    public wh_Expr getWh_expr() {
        return wh_expr;
    }

    public void setWh_expr(wh_Expr wh_expr) {
        this.wh_expr = wh_expr;
    }
    public wh_If getWh_if() {
        return wh_if;
    }

    public void setWh_if(wh_If wh_if) {
        this.wh_if = wh_if;
    }

}