





import java.util.List;
import java.util.ArrayList;

public class simpliC_ExprCall extends Factor {






    private List<simpliC_Expr> simplic_exprs;




    private simpliC_Function simplic_function;


    public simpliC_ExprCall(
    ) {
        super(
        );
        this.simplic_exprs = new ArrayList<>();
    }

    public simpliC_ExprCall(
        ArrayList<simpliC_Expr> simplic_exprs    ) {
        this.simplic_exprs = simplic_exprs;
    }


    public List<simpliC_Expr> getSimplic_exprs() {
        return simplic_exprs;
    }

    public void addSimplic_expr(Simplic_expr simplic_expr) {
        this.simplic_exprs.add(simplic_expr);
    }
    public simpliC_Function getSimplic_function() {
        return simplic_function;
    }

    public void setSimplic_function(simpliC_Function simplic_function) {
        this.simplic_function = simplic_function;
    }

}