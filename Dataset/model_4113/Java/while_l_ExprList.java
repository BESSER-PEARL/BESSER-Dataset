





import java.util.List;
import java.util.ArrayList;

public class while_l_ExprList  {






    private List<while_l_Expr> while_l_exprs;


    public while_l_ExprList(
    ) {
        this.while_l_exprs = new ArrayList<>();
    }

    public while_l_ExprList(
        ArrayList<while_l_Expr> while_l_exprs    ) {
        this.while_l_exprs = while_l_exprs;
    }


    public List<while_l_Expr> getWhile_l_exprs() {
        return while_l_exprs;
    }

    public void addWhile_l_expr(While_l_expr while_l_expr) {
        this.while_l_exprs.add(while_l_expr);
    }

}