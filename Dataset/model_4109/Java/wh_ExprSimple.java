





import java.util.List;
import java.util.ArrayList;

public class wh_ExprSimple  {

    private String strSymb;
    private String str;





    private wh_ExprEq wh_expreq;




    private wh_ExprEq wh_expreq;




    private wh_Expr wh_expr;




    private wh_Expr wh_expr;


    public wh_ExprSimple(
        String strSymb,        String str    ) {
        this.strSymb = strSymb;
        this.str = str;
    }


    public String getStrsymb() {
        return strSymb;
    }

    public void setStrsymb(String strSymb) {
        this.strSymb = strSymb;
    }
    public String getStr() {
        return str;
    }

    public void setStr(String str) {
        this.str = str;
    }

    public wh_ExprEq getWh_expreq() {
        return wh_expreq;
    }

    public void setWh_expreq(wh_ExprEq wh_expreq) {
        this.wh_expreq = wh_expreq;
    }
    public wh_ExprEq getWh_expreq() {
        return wh_expreq;
    }

    public void setWh_expreq(wh_ExprEq wh_expreq) {
        this.wh_expreq = wh_expreq;
    }
    public wh_Expr getWh_expr() {
        return wh_expr;
    }

    public void setWh_expr(wh_Expr wh_expr) {
        this.wh_expr = wh_expr;
    }
    public wh_Expr getWh_expr() {
        return wh_expr;
    }

    public void setWh_expr(wh_Expr wh_expr) {
        this.wh_expr = wh_expr;
    }

}