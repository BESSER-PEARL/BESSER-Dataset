





import java.util.List;
import java.util.ArrayList;

public class py_ExprSym  {

    private String arg1;





    private List<py_Expr> py_exprs;


    public py_ExprSym(
        String arg1    ) {
        this.arg1 = arg1;
        this.py_exprs = new ArrayList<>();
    }

    public py_ExprSym(
        String arg1        ArrayList<py_Expr> py_exprs    ) {
        this.arg1 = arg1;
        this.py_exprs = py_exprs;
    }

    public String getArg1() {
        return arg1;
    }

    public void setArg1(String arg1) {
        this.arg1 = arg1;
    }

    public List<py_Expr> getPy_exprs() {
        return py_exprs;
    }

    public void addPy_expr(Py_expr py_expr) {
        this.py_exprs.add(py_expr);
    }

}