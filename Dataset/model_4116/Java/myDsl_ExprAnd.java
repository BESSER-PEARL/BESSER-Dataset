





import java.util.List;
import java.util.ArrayList;

public class myDsl_ExprAnd  {






    private List<myDsl_ExprOr> mydsl_exprors;




    private myDsl_Expr mydsl_expr;




    private myDsl_ExprOr mydsl_expror;


    public myDsl_ExprAnd(
    ) {
        this.mydsl_exprors = new ArrayList<>();
    }

    public myDsl_ExprAnd(
        ArrayList<myDsl_ExprOr> mydsl_exprors    ) {
        this.mydsl_exprors = mydsl_exprors;
    }


    public List<myDsl_ExprOr> getMydsl_exprors() {
        return mydsl_exprors;
    }

    public void addMydsl_expror(Mydsl_expror mydsl_expror) {
        this.mydsl_exprors.add(mydsl_expror);
    }
    public myDsl_Expr getMydsl_expr() {
        return mydsl_expr;
    }

    public void setMydsl_expr(myDsl_Expr mydsl_expr) {
        this.mydsl_expr = mydsl_expr;
    }
    public myDsl_ExprOr getMydsl_expror() {
        return mydsl_expror;
    }

    public void setMydsl_expror(myDsl_ExprOr mydsl_expror) {
        this.mydsl_expror = mydsl_expror;
    }

}