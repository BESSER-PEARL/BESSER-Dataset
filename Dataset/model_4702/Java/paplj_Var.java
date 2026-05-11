





import java.util.List;
import java.util.ArrayList;

public class paplj_Var extends Expr {

    private boolean methodInvocation;





    private List<paplj_Expr> paplj_exprs;




    private paplj_Symbol paplj_symbol;


    public paplj_Var(
        boolean methodInvocation    ) {
        super(
        );
        this.methodInvocation = methodInvocation;
        this.paplj_exprs = new ArrayList<>();
    }

    public paplj_Var(
        boolean methodInvocation        ArrayList<paplj_Expr> paplj_exprs    ) {
        this.methodInvocation = methodInvocation;
        this.paplj_exprs = paplj_exprs;
    }

    public boolean getMethodinvocation() {
        return methodInvocation;
    }

    public void setMethodinvocation(boolean methodInvocation) {
        this.methodInvocation = methodInvocation;
    }

    public List<paplj_Expr> getPaplj_exprs() {
        return paplj_exprs;
    }

    public void addPaplj_expr(Paplj_expr paplj_expr) {
        this.paplj_exprs.add(paplj_expr);
    }
    public paplj_Symbol getPaplj_symbol() {
        return paplj_symbol;
    }

    public void setPaplj_symbol(paplj_Symbol paplj_symbol) {
        this.paplj_symbol = paplj_symbol;
    }

}