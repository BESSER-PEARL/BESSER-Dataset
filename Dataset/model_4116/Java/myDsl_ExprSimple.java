





import java.util.List;
import java.util.ArrayList;

public class myDsl_ExprSimple  {

    private String symbole;
    private String variable;
    private String vide;





    private myDsl_Expr mydsl_expr;


    public myDsl_ExprSimple(
        String symbole,        String variable,        String vide    ) {
        this.symbole = symbole;
        this.variable = variable;
        this.vide = vide;
    }


    public String getSymbole() {
        return symbole;
    }

    public void setSymbole(String symbole) {
        this.symbole = symbole;
    }
    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }
    public String getVide() {
        return vide;
    }

    public void setVide(String vide) {
        this.vide = vide;
    }

    public myDsl_Expr getMydsl_expr() {
        return mydsl_expr;
    }

    public void setMydsl_expr(myDsl_Expr mydsl_expr) {
        this.mydsl_expr = mydsl_expr;
    }

}