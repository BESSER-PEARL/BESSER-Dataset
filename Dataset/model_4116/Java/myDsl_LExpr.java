





import java.util.List;
import java.util.ArrayList;

public class myDsl_LExpr  {






    private myDsl_Cons mydsl_cons;




    private myDsl_SymboleEx mydsl_symboleex;




    private myDsl_Liste mydsl_liste;




    private List<myDsl_Expr> mydsl_exprs;


    public myDsl_LExpr(
    ) {
        this.mydsl_exprs = new ArrayList<>();
    }

    public myDsl_LExpr(
        ArrayList<myDsl_Expr> mydsl_exprs    ) {
        this.mydsl_exprs = mydsl_exprs;
    }


    public myDsl_Cons getMydsl_cons() {
        return mydsl_cons;
    }

    public void setMydsl_cons(myDsl_Cons mydsl_cons) {
        this.mydsl_cons = mydsl_cons;
    }
    public myDsl_SymboleEx getMydsl_symboleex() {
        return mydsl_symboleex;
    }

    public void setMydsl_symboleex(myDsl_SymboleEx mydsl_symboleex) {
        this.mydsl_symboleex = mydsl_symboleex;
    }
    public myDsl_Liste getMydsl_liste() {
        return mydsl_liste;
    }

    public void setMydsl_liste(myDsl_Liste mydsl_liste) {
        this.mydsl_liste = mydsl_liste;
    }
    public List<myDsl_Expr> getMydsl_exprs() {
        return mydsl_exprs;
    }

    public void addMydsl_expr(Mydsl_expr mydsl_expr) {
        this.mydsl_exprs.add(mydsl_expr);
    }

}