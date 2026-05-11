





import java.util.List;
import java.util.ArrayList;

public class fl_Function  {

    private String name;
    private String arg;





    private fl_Expr fl_expr;




    private fl_ProgramType fl_programtype;


    public fl_Function(
        String name,        String arg    ) {
        this.name = name;
        this.arg = arg;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getArg() {
        return arg;
    }

    public void setArg(String arg) {
        this.arg = arg;
    }

    public fl_Expr getFl_expr() {
        return fl_expr;
    }

    public void setFl_expr(fl_Expr fl_expr) {
        this.fl_expr = fl_expr;
    }
    public fl_ProgramType getFl_programtype() {
        return fl_programtype;
    }

    public void setFl_programtype(fl_ProgramType fl_programtype) {
        this.fl_programtype = fl_programtype;
    }

}