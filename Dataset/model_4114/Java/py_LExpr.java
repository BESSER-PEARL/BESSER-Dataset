





import java.util.List;
import java.util.ArrayList;

public class py_LExpr  {






    private py_ExprCons py_exprcons;




    private List<py_Expr> py_exprs;


    public py_LExpr(
    ) {
        this.py_exprs = new ArrayList<>();
    }

    public py_LExpr(
        ArrayList<py_Expr> py_exprs    ) {
        this.py_exprs = py_exprs;
    }


    public py_ExprCons getPy_exprcons() {
        return py_exprcons;
    }

    public void setPy_exprcons(py_ExprCons py_exprcons) {
        this.py_exprcons = py_exprcons;
    }
    public List<py_Expr> getPy_exprs() {
        return py_exprs;
    }

    public void addPy_expr(Py_expr py_expr) {
        this.py_exprs.add(py_expr);
    }

}