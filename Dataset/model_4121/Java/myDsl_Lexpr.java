





import java.util.List;
import java.util.ArrayList;

public class myDsl_Lexpr  {






    private myDsl_ExprSimple mydsl_exprsimple;




    private List<myDsl_Expr> mydsl_exprs;


    public myDsl_Lexpr(
    ) {
        this.mydsl_exprs = new ArrayList<>();
    }

    public myDsl_Lexpr(
        ArrayList<myDsl_Expr> mydsl_exprs    ) {
        this.mydsl_exprs = mydsl_exprs;
    }


    public myDsl_ExprSimple getMydsl_exprsimple() {
        return mydsl_exprsimple;
    }

    public void setMydsl_exprsimple(myDsl_ExprSimple mydsl_exprsimple) {
        this.mydsl_exprsimple = mydsl_exprsimple;
    }
    public List<myDsl_Expr> getMydsl_exprs() {
        return mydsl_exprs;
    }

    public void addMydsl_expr(Mydsl_expr mydsl_expr) {
        this.mydsl_exprs.add(mydsl_expr);
    }

}