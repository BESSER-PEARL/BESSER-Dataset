





import java.util.List;
import java.util.ArrayList;

public class limp_AssignmentStatement extends Statement, Equation {






    private limp_Expr limp_expr;


    public limp_AssignmentStatement(
    ) {
        super(
        );
    }



    public limp_Expr getLimp_expr() {
        return limp_expr;
    }

    public void setLimp_expr(limp_Expr limp_expr) {
        this.limp_expr = limp_expr;
    }

}