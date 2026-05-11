





import java.util.List;
import java.util.ArrayList;

public class imp_ArrayDecl extends Expr {






    private List<imp_Expr> imp_exprs;


    public imp_ArrayDecl(
    ) {
        super(
        );
        this.imp_exprs = new ArrayList<>();
    }

    public imp_ArrayDecl(
        ArrayList<imp_Expr> imp_exprs    ) {
        this.imp_exprs = imp_exprs;
    }


    public List<imp_Expr> getImp_exprs() {
        return imp_exprs;
    }

    public void addImp_expr(Imp_expr imp_expr) {
        this.imp_exprs.add(imp_expr);
    }

}