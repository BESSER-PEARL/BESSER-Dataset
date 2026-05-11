





import java.util.List;
import java.util.ArrayList;

public class wh_ExprEq  {

    private String sym;





    private wh_ExprSimple wh_exprsimple;




    private wh_Expr wh_expr;




    private wh_LExpr wh_lexpr;




    private wh_ExprSimple wh_exprsimple;




    private wh_ExprNot wh_exprnot;


    public wh_ExprEq(
        String sym    ) {
        this.sym = sym;
    }


    public String getSym() {
        return sym;
    }

    public void setSym(String sym) {
        this.sym = sym;
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
    public wh_LExpr getWh_lexpr() {
        return wh_lexpr;
    }

    public void setWh_lexpr(wh_LExpr wh_lexpr) {
        this.wh_lexpr = wh_lexpr;
    }
    public wh_ExprSimple getWh_exprsimple() {
        return wh_exprsimple;
    }

    public void setWh_exprsimple(wh_ExprSimple wh_exprsimple) {
        this.wh_exprsimple = wh_exprsimple;
    }
    public wh_ExprNot getWh_exprnot() {
        return wh_exprnot;
    }

    public void setWh_exprnot(wh_ExprNot wh_exprnot) {
        this.wh_exprnot = wh_exprnot;
    }

}