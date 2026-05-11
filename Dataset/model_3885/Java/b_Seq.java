





import java.util.List;
import java.util.ArrayList;

public class b_Seq extends Body, BeginBody {






    private List<b_Expr> b_exprs;




    private b_Var b_var;


    public b_Seq(
    ) {
        super(
        );
        this.b_exprs = new ArrayList<>();
    }

    public b_Seq(
        ArrayList<b_Expr> b_exprs    ) {
        this.b_exprs = b_exprs;
    }


    public List<b_Expr> getB_exprs() {
        return b_exprs;
    }

    public void addB_expr(B_expr b_expr) {
        this.b_exprs.add(b_expr);
    }
    public b_Var getB_var() {
        return b_var;
    }

    public void setB_var(b_Var b_var) {
        this.b_var = b_var;
    }

}