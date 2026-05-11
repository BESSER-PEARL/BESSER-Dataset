





import java.util.List;
import java.util.ArrayList;

public class py_ExprList  {






    private List<py_Expr> py_exprs;


    public py_ExprList(
    ) {
        this.py_exprs = new ArrayList<>();
    }

    public py_ExprList(
        ArrayList<py_Expr> py_exprs    ) {
        this.py_exprs = py_exprs;
    }


    public List<py_Expr> getPy_exprs() {
        return py_exprs;
    }

    public void addPy_expr(Py_expr py_expr) {
        this.py_exprs.add(py_expr);
    }

}