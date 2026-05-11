





import java.util.List;
import java.util.ArrayList;

public class fl_Function  {

    private String arg;
    private String name;





    private fl_ProgramType fl_programtype;




    private fl_Expr fl_expr;


    public fl_Function(
        String arg,        String name    ) {
        this.arg = arg;
        this.name = name;
    }


    public String getArg() {
        return arg;
    }

    public void setArg(String arg) {
        this.arg = arg;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fl_ProgramType getFl_programtype() {
        return fl_programtype;
    }

    public void setFl_programtype(fl_ProgramType fl_programtype) {
        this.fl_programtype = fl_programtype;
    }
    public fl_Expr getFl_expr() {
        return fl_expr;
    }

    public void setFl_expr(fl_Expr fl_expr) {
        this.fl_expr = fl_expr;
    }

}