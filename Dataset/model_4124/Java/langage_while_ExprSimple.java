





import java.util.List;
import java.util.ArrayList;

public class langage_while_ExprSimple  {

    private String nil;
    private String mot;





    private langage_while_Expr langage_while_expr;




    private langage_while_SYMB langage_while_symb;




    private langage_while_LExpr langage_while_lexpr;




    private langage_while_Expr langage_while_expr;




    private langage_while_VAR langage_while_var;


    public langage_while_ExprSimple(
        String nil,        String mot    ) {
        this.nil = nil;
        this.mot = mot;
    }


    public String getNil() {
        return nil;
    }

    public void setNil(String nil) {
        this.nil = nil;
    }
    public String getMot() {
        return mot;
    }

    public void setMot(String mot) {
        this.mot = mot;
    }

    public langage_while_Expr getLangage_while_expr() {
        return langage_while_expr;
    }

    public void setLangage_while_expr(langage_while_Expr langage_while_expr) {
        this.langage_while_expr = langage_while_expr;
    }
    public langage_while_SYMB getLangage_while_symb() {
        return langage_while_symb;
    }

    public void setLangage_while_symb(langage_while_SYMB langage_while_symb) {
        this.langage_while_symb = langage_while_symb;
    }
    public langage_while_LExpr getLangage_while_lexpr() {
        return langage_while_lexpr;
    }

    public void setLangage_while_lexpr(langage_while_LExpr langage_while_lexpr) {
        this.langage_while_lexpr = langage_while_lexpr;
    }
    public langage_while_Expr getLangage_while_expr() {
        return langage_while_expr;
    }

    public void setLangage_while_expr(langage_while_Expr langage_while_expr) {
        this.langage_while_expr = langage_while_expr;
    }
    public langage_while_VAR getLangage_while_var() {
        return langage_while_var;
    }

    public void setLangage_while_var(langage_while_VAR langage_while_var) {
        this.langage_while_var = langage_while_var;
    }

}