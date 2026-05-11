





import java.util.List;
import java.util.ArrayList;

public class wh_ExprSimple  {

    private String sym;
    private String nil;
    private String variable;





    private wh_LExpr wh_lexpr;




    private wh_Expr wh_expr;




    private wh_LExpr wh_lexpr;




    private wh_Expr wh_expr;


    public wh_ExprSimple(
        String sym,        String nil,        String variable    ) {
        this.sym = sym;
        this.nil = nil;
        this.variable = variable;
    }


    public String getSym() {
        return sym;
    }

    public void setSym(String sym) {
        this.sym = sym;
    }
    public String getNil() {
        return nil;
    }

    public void setNil(String nil) {
        this.nil = nil;
    }
    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }

    public wh_LExpr getWh_lexpr() {
        return wh_lexpr;
    }

    public void setWh_lexpr(wh_LExpr wh_lexpr) {
        this.wh_lexpr = wh_lexpr;
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
    public wh_Expr getWh_expr() {
        return wh_expr;
    }

    public void setWh_expr(wh_Expr wh_expr) {
        this.wh_expr = wh_expr;
    }

}