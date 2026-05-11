





import java.util.List;
import java.util.ArrayList;

public class py_Expr  {






    private py_EObject py_eobject;




    private py_ExprAnd py_exprand;




    private py_If py_if;


    public py_Expr(
    ) {
    }



    public py_EObject getPy_eobject() {
        return py_eobject;
    }

    public void setPy_eobject(py_EObject py_eobject) {
        this.py_eobject = py_eobject;
    }
    public py_ExprAnd getPy_exprand() {
        return py_exprand;
    }

    public void setPy_exprand(py_ExprAnd py_exprand) {
        this.py_exprand = py_exprand;
    }
    public py_If getPy_if() {
        return py_if;
    }

    public void setPy_if(py_If py_if) {
        this.py_if = py_if;
    }

}