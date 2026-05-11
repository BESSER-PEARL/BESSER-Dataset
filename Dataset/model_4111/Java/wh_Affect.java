





import java.util.List;
import java.util.ArrayList;

public class wh_Affect  {

    private String vars;





    private List<wh_Expr> wh_exprs;


    public wh_Affect(
        String vars    ) {
        this.vars = vars;
        this.wh_exprs = new ArrayList<>();
    }

    public wh_Affect(
        String vars        ArrayList<wh_Expr> wh_exprs    ) {
        this.vars = vars;
        this.wh_exprs = wh_exprs;
    }

    public String getVars() {
        return vars;
    }

    public void setVars(String vars) {
        this.vars = vars;
    }

    public List<wh_Expr> getWh_exprs() {
        return wh_exprs;
    }

    public void addWh_expr(Wh_expr wh_expr) {
        this.wh_exprs.add(wh_expr);
    }

}