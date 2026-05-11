





import java.util.List;
import java.util.ArrayList;

public class miniJava_MethodCall  {






    private miniJava_Method minijava_method;




    private miniJava_Expr minijava_expr;




    private List<miniJava_Expr> minijava_exprs;


    public miniJava_MethodCall(
    ) {
        this.minijava_exprs = new ArrayList<>();
    }

    public miniJava_MethodCall(
        ArrayList<miniJava_Expr> minijava_exprs    ) {
        this.minijava_exprs = minijava_exprs;
    }


    public miniJava_Method getMinijava_method() {
        return minijava_method;
    }

    public void setMinijava_method(miniJava_Method minijava_method) {
        this.minijava_method = minijava_method;
    }
    public miniJava_Expr getMinijava_expr() {
        return minijava_expr;
    }

    public void setMinijava_expr(miniJava_Expr minijava_expr) {
        this.minijava_expr = minijava_expr;
    }
    public List<miniJava_Expr> getMinijava_exprs() {
        return minijava_exprs;
    }

    public void addMinijava_expr(Minijava_expr minijava_expr) {
        this.minijava_exprs.add(minijava_expr);
    }

}