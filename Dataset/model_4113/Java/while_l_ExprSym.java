





import java.util.List;
import java.util.ArrayList;

public class while_l_ExprSym  {

    private String arg1;





    private List<while_l_Expr> while_l_exprs;


    public while_l_ExprSym(
        String arg1    ) {
        this.arg1 = arg1;
        this.while_l_exprs = new ArrayList<>();
    }

    public while_l_ExprSym(
        String arg1        ArrayList<while_l_Expr> while_l_exprs    ) {
        this.arg1 = arg1;
        this.while_l_exprs = while_l_exprs;
    }

    public String getArg1() {
        return arg1;
    }

    public void setArg1(String arg1) {
        this.arg1 = arg1;
    }

    public List<while_l_Expr> getWhile_l_exprs() {
        return while_l_exprs;
    }

    public void addWhile_l_expr(While_l_expr while_l_expr) {
        this.while_l_exprs.add(while_l_expr);
    }

}