





import java.util.List;
import java.util.ArrayList;

public class robotG_flow_Programme  {






    private List<Expr> exprs;


    public robotG_flow_Programme(
    ) {
        this.exprs = new ArrayList<>();
    }

    public robotG_flow_Programme(
        ArrayList<Expr> exprs    ) {
        this.exprs = exprs;
    }


    public List<Expr> getExprs() {
        return exprs;
    }

    public void addExpr(Expr expr) {
        this.exprs.add(expr);
    }

}