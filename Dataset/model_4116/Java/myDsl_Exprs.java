





import java.util.List;
import java.util.ArrayList;

public class myDsl_Exprs  {






    private myDsl_Expr mydsl_expr;




    private myDsl_AffectVar mydsl_affectvar;




    private List<myDsl_Expr> mydsl_exprs;


    public myDsl_Exprs(
    ) {
        this.mydsl_exprs = new ArrayList<>();
    }

    public myDsl_Exprs(
        ArrayList<myDsl_Expr> mydsl_exprs    ) {
        this.mydsl_exprs = mydsl_exprs;
    }


    public myDsl_Expr getMydsl_expr() {
        return mydsl_expr;
    }

    public void setMydsl_expr(myDsl_Expr mydsl_expr) {
        this.mydsl_expr = mydsl_expr;
    }
    public myDsl_AffectVar getMydsl_affectvar() {
        return mydsl_affectvar;
    }

    public void setMydsl_affectvar(myDsl_AffectVar mydsl_affectvar) {
        this.mydsl_affectvar = mydsl_affectvar;
    }
    public List<myDsl_Expr> getMydsl_exprs() {
        return mydsl_exprs;
    }

    public void addMydsl_expr(Mydsl_expr mydsl_expr) {
        this.mydsl_exprs.add(mydsl_expr);
    }

}