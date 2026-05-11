





import java.util.List;
import java.util.ArrayList;

public class py_Affect  {

    private String vars;





    private List<py_Expr> py_exprs;


    public py_Affect(
        String vars    ) {
        this.vars = vars;
        this.py_exprs = new ArrayList<>();
    }

    public py_Affect(
        String vars        ArrayList<py_Expr> py_exprs    ) {
        this.vars = vars;
        this.py_exprs = py_exprs;
    }

    public String getVars() {
        return vars;
    }

    public void setVars(String vars) {
        this.vars = vars;
    }

    public List<py_Expr> getPy_exprs() {
        return py_exprs;
    }

    public void addPy_expr(Py_expr py_expr) {
        this.py_exprs.add(py_expr);
    }

}