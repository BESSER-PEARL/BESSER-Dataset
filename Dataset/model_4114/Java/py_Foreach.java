





import java.util.List;
import java.util.ArrayList;

public class py_Foreach  {

    private String var;





    private py_Expr py_expr;




    private py_Commands py_commands;


    public py_Foreach(
        String var    ) {
        this.var = var;
    }


    public String getVar() {
        return var;
    }

    public void setVar(String var) {
        this.var = var;
    }

    public py_Expr getPy_expr() {
        return py_expr;
    }

    public void setPy_expr(py_Expr py_expr) {
        this.py_expr = py_expr;
    }
    public py_Commands getPy_commands() {
        return py_commands;
    }

    public void setPy_commands(py_Commands py_commands) {
        this.py_commands = py_commands;
    }

}