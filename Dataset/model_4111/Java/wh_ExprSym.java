





import java.util.List;
import java.util.ArrayList;

public class wh_ExprSym extends Expr {

    private String arg1;





    private List<wh_Expr> wh_exprs;


    public wh_ExprSym(
        String arg1    ) {
        super(
        );
        this.arg1 = arg1;
        this.wh_exprs = new ArrayList<>();
    }

    public wh_ExprSym(
        String arg1        ArrayList<wh_Expr> wh_exprs    ) {
        this.arg1 = arg1;
        this.wh_exprs = wh_exprs;
    }

    public String getArg1() {
        return arg1;
    }

    public void setArg1(String arg1) {
        this.arg1 = arg1;
    }

    public List<wh_Expr> getWh_exprs() {
        return wh_exprs;
    }

    public void addWh_expr(Wh_expr wh_expr) {
        this.wh_exprs.add(wh_expr);
    }

}