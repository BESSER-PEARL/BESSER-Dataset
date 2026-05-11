





import java.util.List;
import java.util.ArrayList;

public class Legolang_controlflow_Program  {






    private List<Expr> exprs;


    public Legolang_controlflow_Program(
    ) {
        this.exprs = new ArrayList<>();
    }

    public Legolang_controlflow_Program(
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