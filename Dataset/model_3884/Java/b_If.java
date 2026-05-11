





import java.util.List;
import java.util.ArrayList;

public class b_If extends Expr, Body, FinalExpr {






    private b_Expr b_expr;


    public b_If(
    ) {
        super(
        );
    }



    public b_Expr getB_expr() {
        return b_expr;
    }

    public void setB_expr(b_Expr b_expr) {
        this.b_expr = b_expr;
    }

}