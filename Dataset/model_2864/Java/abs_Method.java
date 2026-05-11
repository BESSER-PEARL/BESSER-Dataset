





import java.util.List;
import java.util.ArrayList;

public class abs_Method  {

    private String name;





    private abs_Class_decl abs_class_decl;




    private abs_Type_use abs_type_use;




    private List<abs_Stmt> abs_stmts;




    private abs_Param_list abs_param_list;


    public abs_Method(
        String name    ) {
        this.name = name;
        this.abs_stmts = new ArrayList<>();
    }

    public abs_Method(
        String name        ArrayList<abs_Stmt> abs_stmts    ) {
        this.name = name;
        this.abs_stmts = abs_stmts;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public abs_Class_decl getAbs_class_decl() {
        return abs_class_decl;
    }

    public void setAbs_class_decl(abs_Class_decl abs_class_decl) {
        this.abs_class_decl = abs_class_decl;
    }
    public abs_Type_use getAbs_type_use() {
        return abs_type_use;
    }

    public void setAbs_type_use(abs_Type_use abs_type_use) {
        this.abs_type_use = abs_type_use;
    }
    public List<abs_Stmt> getAbs_stmts() {
        return abs_stmts;
    }

    public void addAbs_stmt(Abs_stmt abs_stmt) {
        this.abs_stmts.add(abs_stmt);
    }
    public abs_Param_list getAbs_param_list() {
        return abs_param_list;
    }

    public void setAbs_param_list(abs_Param_list abs_param_list) {
        this.abs_param_list = abs_param_list;
    }

}